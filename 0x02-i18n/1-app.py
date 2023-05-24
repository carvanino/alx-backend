#!/urs/bin/env python3
"""
Babel-Flask extension and setup
"""

from flask import Flask, render_template
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


@app.route('/')
def index_1():
    """
    Renders templates/1-index.html
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5007)
