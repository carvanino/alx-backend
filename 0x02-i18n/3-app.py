#!/usr/bin/env python3
"""
Babel-Flask extension and setup
Get locale from request
Parameterize Templates
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _


app = Flask(__name__)


class Config(object):
    """
    Configues available languages in our app
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Determines the users preferred match from app supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index_1():
    """
    Renders templates/1-index.html
    """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5007)
