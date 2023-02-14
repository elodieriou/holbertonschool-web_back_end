#!/usr/bin/env python3
"""Auth module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from typing import Type
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    """ Hash password
    """
    convert = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(convert, salt)

    return hashed_password


def _generate_uuid() -> str:
    """ Generate new UUID
    """
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Initialized
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Register a user
        """
        try:
            user: Type[User] = self._db.find_user_by(email=email)
            if user is not None:
                raise ValueError("User {} already exists".format(user.email))
        except NoResultFound:
            decode_password: str = _hash_password(password).decode()
            new_user: User = self._db.add_user(email, decode_password)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """ Check password
        """
        try:
            user: Type[User] = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        pwd: bytes = password.encode('utf-8')
        db_pwd: bytes = user.hashed_password.encode('utf-8')
        return bcrypt.checkpw(pwd, db_pwd)
