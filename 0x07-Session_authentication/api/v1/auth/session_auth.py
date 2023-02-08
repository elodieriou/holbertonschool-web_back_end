#!/usr/bin/env python3
""" Module of Session Authentication
"""
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """Class SessionAuth defines the followings methods:
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ This method create a Session ID for a user_id
        :param user_id: the user ID
        :return: None or Create a Session ID
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
