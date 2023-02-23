#!/usr/bin/env python3
""" Flask app """
import pytz
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict


app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """ Supported languages list """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """ Use the locale language """
    languages = app.config['LANGUAGES']

    try:
        locale = request.args.get('locale')
        if locale and locale in languages:
            return locale

        user_locale = g.user['locale']
        if user_locale and user_locale in languages:
            return user_locale
    except Exception:
        pass

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.before_request
def before_request() -> None:
    """ Method run before all request """
    user = get_user()
    if user:
        g.user = user


def get_user() -> Dict:
    """ Retrieve the user thanks its ID """
    try:
        user_id = int(request.args.get('login_as'))
        if user_id in users.keys():
            return users[user_id]
    except Exception:
        return None


@app.route("/", methods=['GET'])
def welcome() -> str:
    """ Message of Welcome """
    try:
        username = g.user['name']
    except Exception:
        username = None

    return render_template('6-index.html', username=username)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
