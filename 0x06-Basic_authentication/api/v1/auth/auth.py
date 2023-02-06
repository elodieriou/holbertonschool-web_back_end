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
        """ This method checks if path require authentication
        :param path: the route check
        :param excluded_paths: list of route
        :return: True or False if the route check require authentication
        """
        if path is None or excluded_paths is None or excluded_paths is []:
            return True

        for excluded_path in excluded_paths:
            if path.startswith(excluded_path) or path + '/' == excluded_path:
                return False

        return True

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
