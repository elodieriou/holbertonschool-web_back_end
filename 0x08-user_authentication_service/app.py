#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, jsonify, request, abort, redirect
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
    email: str = request.form.get('email')
    password: str = request.form.get('password')
    if not email or not password:
        return abort(401)

    check_password: bool = AUTH.valid_login(email=email, password=password)
    if not check_password:
        abort(401)

    session_id: str = AUTH.create_session(email=email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie("session_id", session_id)
    return response


@app.route("/sessions", methods=['DELETE'], strict_slashes=False)
def logout():
    """ DELETE /sessions """
    session_id = request.cookies.get("session_id")
    if not session_id:
        abort(403)

    try:
        user = AUTH.get_user_from_session_id(session_id)
        AUTH.destroy_session(user_id=user.id)
    except Exception:
        return abort(403)

    return redirect("/", 301)


@app.route("/profile", methods=['GET'], strict_slashes=False)
def profile() -> str:
    """ GET /profile
    """

    session_id = request.cookies.get("session_id")
    if not session_id:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)

    return jsonify({"email": user.email}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
