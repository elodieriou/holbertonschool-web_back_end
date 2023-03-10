#!/usr/bin/env python3
"""Auth module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
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
            user: User = self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(user.email))
        except NoResultFound:
            decode_password: str = _hash_password(password).decode()
            new_user: User = self._db.add_user(email, decode_password)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """ Check password
        """
        try:
            user: User = self._db.find_user_by(email=email)
            pwd: bytes = password.encode('utf-8')
            db_pwd: bytes = user.hashed_password.encode('utf-8')
            return bcrypt.checkpw(pwd, db_pwd)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """ Create session
        """
        try:
            user: User = self._db.find_user_by(email=email)
            session_id: str = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """ Find user thanks its session_id
        """
        if session_id is None:
            return None

        try:
            user: User = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """ Destroy session
        """
        if user_id is None:
            return None

        try:
            user: User = self._db.find_user_by(id=user_id)
            self._db.update_user(user.id, session_id=None)
        except NoResultFound:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """ Generate reset password token
        """
        if email is None:
            return None

        try:
            user: User = self._db.find_user_by(email=email)
            token: str = _generate_uuid()
            self._db.update_user(user.id, reset_token=token)
            return token
        except Exception:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """ Update password
        """
        try:
            user: User = self._db.find_user_by(reset_token=reset_token)
            hash_pwd: str = _hash_password(password).decode()
            self._db.update_user(user.id,
                                 hashed_password=hash_pwd,
                                 reset_token=None)
        except Exception:
            raise ValueError
