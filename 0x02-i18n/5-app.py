#!/usr/bin/env python3
"""
Babel-Flask extension and setup
Get locale from request
Parameterize Templates
Mock logging in
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)


class Config(object):
    """
    Configues available languages in our app
    """

    LANGUAGES = ["en", "fr"]
    BABEL_default_locale = "en"
    BABEL_default_timezone = "UTC"


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
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """
    Returns a users dictionary or None
    """
    login = request.args.get('login_as', '')
    if login:
        return users[int(login)]
    return None


@app.before_request
def before_request():
    """
    """
    user = get_user()
    if user is not None:
        setattr(g, 'user', user)


@app.route('/')
def index_1():
    """
    Renders templates/1-index.html
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5007)
