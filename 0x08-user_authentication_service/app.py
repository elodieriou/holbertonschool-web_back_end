#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, jsonify, request, abort
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/")
def bienvenue() -> str:
    """ Message of Bienvenue """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'], strict_slashes=False)
def users() -> str:
    """ POST /users """
    email: str = request.form.get('email')
    password: str = request.form.get('password')

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=['POST'], strict_slashes=False)
def login() -> str:
    """ POST /sessions """
    try:
        email: str = request.form.get('email')
        password: str = request.form.get('password')
    except Exception:
        return abort(401)

    check_password: bool = AUTH.valid_login(email=email, password=password)
    if check_password:
        session_id: str = AUTH.create_session(email=email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response
    else:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
