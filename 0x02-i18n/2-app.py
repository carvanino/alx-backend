#!/urs/bin/env python3
"""
Babel-Flask extension and setup
Get locale from request
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
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5007)
