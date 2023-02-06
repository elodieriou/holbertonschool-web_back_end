#!/usr/bin/env python3
""" Module of Authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Class Auth defines the following methods:
    - require_auth : return a boolean
    - authorization_header : return the header
    - current_user : return the user object
    """

    User = TypeVar('User')

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        :param path:
        :param excluded_paths:
        :return:
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        :param request:
        :return:
        """
        return request

    def current_user(self, request=None) -> User:
        """
        :param request:
        :return:
        """
        return request
