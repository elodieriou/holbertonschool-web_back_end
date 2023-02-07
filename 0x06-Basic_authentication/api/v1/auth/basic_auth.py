#!/usr/bin/env python3
""" Module of Basic Authentication
"""
from api.v1.auth.auth import Auth
from base64 import b64decode
from typing import List, TypeVar
from models.user import User


class BasicAuth(Auth):
    """Class BasicAuth defines the following methods:
    - extract_base64_authorization_header: returns the Base64 part of
    the Authorization header for a Basic Authentication
    - decode_base64_authorization_header: returns the decoded value of
    a Base64 string
    - extract_user_credentials: returns the user email and password from
    the Base64
    - user_object_from_credentials: returns the User instance based on his
    email and password
    - current_user: retrieves the User instance for a request
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str)\
            -> str:
        """ This method returns the base64 string of a Basic Authentication
        :param authorization_header: the authorization header
        :return: None or base64 string if it is a Basic Authentication
        """

        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith('Basic '):
            return None

        return authorization_header.split("Basic ")[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str)\
            -> str:
        """ This method returns the decoded value of a Base64 string
        :param base64_authorization_header:
        :return: None or decode base64 string if it is a Basic Authentication
        """

        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            return b64decode(base64_authorization_header).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str) \
            -> (str, str):
        """ This method returns the user email and password from the Base64
        decode value
        :param decoded_base64_authorization_header: the header decode
        :return: None or the email and password
        """

        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        match: List = decoded_base64_authorization_header.split(':', 1)
        if len(match) != 2:
            return None, None

        return match[0], match[1]

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str)\
            -> TypeVar('User'):
        """ This method returns the User instance based on his email and
        password
        :param user_email: the email of the user
        :param user_pwd: the password of the user
        :return: None or User instance
        """

        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            users: List = User.search({"email": user_email})
        except Exception:
            return None

        for user in users:
            check: bool = user.is_valid_password(user_pwd)
            if check:
                return user

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ This method retrieves the User instance for a request
        :param request: the request
        :return: None or the current User
        """
        header = Auth.authorization_header(self, request)
        encode = BasicAuth.extract_base64_authorization_header(self, header)
        decode = BasicAuth.decode_base64_authorization_header(self, encode)
        extract = BasicAuth.extract_user_credentials(self, decode)
        user = BasicAuth.user_object_from_credentials(self,
                                                      extract[0],
                                                      extract[1])
        return user
