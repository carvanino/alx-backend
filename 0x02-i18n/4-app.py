#!/usr/bin/env python3
"""
Babel-Flask extension and setup
Get locale from request
Parameterize Templates
"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config(object):
    """
    Configues available languages in our app
    """

    LANGUAGES = ["en", "fr"]
    BABEL_default_locale = "en"
    BABEL_default_timezone = "UTC"


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
    print(locale)
    if locale and locale in app.config['LANGUAGES']:
        print(locale)
        return locale
    print(locale)
    return request.accept_languages.best_match(app.config['LANGUAGES'])
    # return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index_1():
    """
    Renders templates/1-index.html
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5007)
