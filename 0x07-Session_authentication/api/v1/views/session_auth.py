#!/usr/bin/env python3
""" Module of Sessions views
"""
from api.v1.views import app_views
from flask import jsonify, request
from typing import List
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ POST /api/v1/auth_session/login/
    JSON body:
      - email
      - password
      - last_name (optional)
      - first_name (optional)
    Return:
      - User object JSON represented
      - 400 if can't create the new session
    """
    email: str = request.form.get('email')
    if email == "" or not email:
        return jsonify({"error": "email missing"}), 400

    password: str = request.form.get('password')
    if password == "" or not password:
        return jsonify({"error": "password missing"}), 400

    try:
        users: List = User.search({'email': email})
        if not users:
            return jsonify({"error": "no user found for this email"}), 404
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404

    for user in users:
        check: bool = user.is_valid_password(password)
        if not check:
            return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    user = users[0]
    user_id = user.id
    session_id = auth.create_session(user_id)

    cookie_name = getenv('SESSION_NAME')
    response = jsonify(user.to_json())
    response.set_cookie(cookie_name, session_id)

    return response
