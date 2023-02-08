#!/usr/bin/env python3
""" Module of Authentication
"""
from flask import request
from typing import List, TypeVar
import re
from os import getenv


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
            check: List = excluded_path.split('*')
            if path.startswith(check[0]) or path + '/' == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ This method return the value of the header request
        :param request: the route requested
        :return: None or the header of the request
        """
        if request is None:
            return None

        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> User:
        """
        :param request:
        :return:
        """
        return None

    def session_cookie(self, request=None):
        """ This method returns a cookie value from a request
        :param request: the request
        :return: None or value of the cookie named _my_session_id
        """

        if request is None:
            return None

        SESSION_NAME = getenv('SESSION_NAME')
        return request.cookies.get(SESSION_NAME)
