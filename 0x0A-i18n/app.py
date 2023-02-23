#!/usr/bin/env python3
""" Flask app """
import locale
import datetime
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


@babel.timezoneselector
def get_timezone() -> str:
    """ Use the timezone """
    default_timezone = app.config["BABEL_DEFAULT_LOCALE"]

    try:
        timezone = request.args.get('timezone')
        if timezone and pytz.timezone(timezone):
            return timezone

        user_timezone = g.user['timezone']
        if user_timezone and pytz.timezone(user_timezone):
            return user_timezone
    except pytz.exceptions.UnknownTimeZoneError:
        return 'UTC'

    return request.accept_languages.best_match(default_timezone)


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
        timezone = get_timezone()
        date = datetime.datetime.now(pytz.timezone(timezone))

        if get_locale() == 'en':
            locale.setlocale(locale.LC_TIME, "en_US.UTF-8")
            format_str = '%b %d, %Y, %I:%M:%S %p'
            current_time = date.strftime(format_str)

        if get_locale() == 'fr':
            locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")
            format_str = '%d %b %Y à %H:%M:%S'
            current_time = date.strftime(format_str)

    except Exception:
        username = None
        current_time = None

    return render_template('7-index.html', username=username, current_time=current_time)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
