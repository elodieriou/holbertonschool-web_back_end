#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, jsonify, request, abort, redirect, make_response
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
        return make_response(redirect("/", 302))
    except Exception:
        return abort(403)


@app.route("/profile", methods=['GET'], strict_slashes=False)
def profile() -> str:
    """ GET /profile
    """

    session_id = request.cookies.get("session_id")
    if not session_id:
        abort(403)

    try:
        user = AUTH.get_user_from_session_id(session_id)
        return jsonify({"email": user.email}), 200
    except Exception:
        abort(403)


@app.route("/reset_password", methods=['POST'], strict_slashes=False)
def get_reset_password_token() -> str:
    """ POST /reset_password
    """
    email: str = request.form.get("email")
    if not email:
        abort(403)

    try:
        token: str = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": token}), 200
    except Exception:
        abort(403)


@app.route("/reset_password", methods=['PUT'], strict_slashes=False)
def update_password() -> str:
    """ PUT /reset_password
    """
    email: str = request.form.get("email")
    token: str = request.form.get("reset_token")
    password: str = request.form.get("new_password")
    if not email or not token or not password:
        abort(403)

    try:
        AUTH.update_password(token, password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except Exception:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
