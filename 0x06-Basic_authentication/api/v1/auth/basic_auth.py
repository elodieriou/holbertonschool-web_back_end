#!/usr/bin/env python3
""" Module of Basic Authentication
"""
from api.v1.auth.auth import Auth
from base64 import b64decode


class BasicAuth(Auth):
    """Class BasicAuth defines the following methods:
    - extract_base64_authorization_header: returns the Base64 part of
     the Authorization header for a Basic Authentication
    """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
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

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
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
        except:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """ This method returns the user email and password from the Base64 decode value
        :param decoded_base64_authorization_header:
        :return:
        """

        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        match = decoded_base64_authorization_header.split(':')
        if len(match) != 2:
            return None, None

        return match[0], match[1]
