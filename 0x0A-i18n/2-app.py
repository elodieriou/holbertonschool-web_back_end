#!/usr/bin/env python3
""" Flask app """
from flask import Flask, render_template, request
from flask_babel import Babel
from typing import List, Optional


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Supported languages list """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route("/", methods=['GET'])
def welcome() -> str:
    """ Message of Welcome """
    return render_template('2-index.html')


@babel.localeselector
def get_local() -> Optional[List]:
    """ Use the locale language """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
