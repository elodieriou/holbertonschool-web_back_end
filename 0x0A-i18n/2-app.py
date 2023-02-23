#!/usr/bin/env python3
"""Route module for the API"""
from flask import Flask, render_template, request
from flask_babel import Babel
from typing import List

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Config class"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> List:
    """
    This function is invoked for each request
    to select a language translation to use for that request
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def hello_world():
    """Route that renders a simple template"""
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run()
