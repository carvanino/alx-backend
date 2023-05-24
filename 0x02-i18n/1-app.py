#!/urs/bin/env python3
"""
Babel-Flask extension and setup
"""

from flask import Flask, render_template
from flask_babel import Babel




class Config:
    """
    Configues available languages in our app
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = FLask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route('/')
def index_1():
    """
    Renders templates/1-index.html
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5007)
