#!/usr/bin/env python3
"""
Babel-Flask extension and setup
Get locale from request
Parameterize Templates
Mock logging in
Infer appropriate time zone
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
import pytz
from pytz import timezone
from pytz.exceptions import UnknownTimeZoneError


app = Flask(__name__)


class Config(object):
    """
    Configues available languages in our app
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Determines the users preferred match from app supported languages
    """
    # checks for the args 'locale' in the url
    # sent through the request and gives an empty string as default value
    # to prevent raising a keyError
    # locale = request.args['locale'] | ''
    locale = request.args.get('locale', '')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    locale = request.headers.get('locale', '')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """
    Returns a users dictionary or None
    """
    login = request.args.get('login_as')
    if login:
        return users[int(login)]
    return None


@app.before_request
def before_request():
    """
    Gets the current user logged in
    """
    g.user = get_user()

    '''
    if user is not None:
        setattr(g, 'user', user)
    '''


@babel.timezoneselector
def get_timezone():
    """
    Gets the timezone from the URL parameters, users settings and validate it
    and the default timezone
    """
    tz = request.args.get('timezone',  '').strip()
    if not tz and g.user:
        tz = g.user['timezone']
    try:
        timezone(tz)
    except UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index_1():
    """
    Renders templates/1-index.html
    """
    g.time = format_datetime()
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5007)
