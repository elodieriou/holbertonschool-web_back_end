#!/usr/bin/env python3
"""Main module
"""
import requests


def register_user(email: str, password: str) -> None:
    """ Check register user
    """
    response = requests.post(url="http://localhost:5000/users",
                             data={"email": email, "password": password})

    data = {"email": email, "message": "user created"}
    assert response.json() == data
    assert response.status_code == 200


def log_in_wrong_password(email: str, password: str) -> None:
    """ Check login password
    """
    response = requests.post(url="http://localhost:5000/sessions",
                             data={"email": email, "password": password})

    assert response.status_code == 401


def log_in(email: str, password: str) -> str:
    """ Check login
    """
    response = requests.post(url="http://localhost:5000/sessions",
                             data={"email": email, "password": password})

    data = {"email": email, "message": "logged in"}
    assert response.json() == data
    assert response.status_code == 200

    return response.cookies.get("session_id")


def profile_unlogged() -> None:
    """ Check profile unlogged
    """
    response = requests.get(url="http://localhost:5000/profile")

    assert response.status_code == 403


def profile_logged(session_id: str) -> None:
    """ Check profile logged
    """
    response = requests.get(url="http://localhost:5000/profile",
                            cookies={"session_id": session_id})

    email = response.json().get("email")
    data = {"email": email}
    assert response.json() == data
    assert response.status_code == 200


def log_out(session_id: str) -> None:
    """ Check logout
    """
    response = requests.delete(url="http://localhost:5000/sessions",
                               cookies={"session_id": session_id},
                               allow_redirects=False)

    assert response.status_code == 302


def reset_password_token(email: str) -> str:
    """ Check reset password token
    """
    response = requests.post(url="http://localhost:5000/reset_password",
                             data={"email": email})

    token = response.json().get("reset_token")
    data = {"email": email, "reset_token": token}
    assert response.json() == data
    assert response.status_code == 200

    return token


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """ Check update password
    """
    response = requests.put(url="http://localhost:5000/reset_password",
                            data={"email": email,
                                  "reset_token": reset_token,
                                  "new_password": new_password})
    data = {"email": email, "message": "Password updated"}
    assert response.json() == data
    assert response.status_code == 200


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
