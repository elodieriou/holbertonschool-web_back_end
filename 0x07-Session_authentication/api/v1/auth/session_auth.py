#!/usr/bin/env python3
""" Module of Session Authentication
"""
from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ This method returns a USer ID based on a Session ID
        :param session_id: the session ID
        :return: None or the user ID
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ This method returns a User instance based on a cookie value
        :param request: the request
        :return: the user ID based on the cookie _my_session_id
        """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)

        return User.get(user_id)

    def destroy_session(self, request=None) -> bool:
        """ This method deletes the user session / logout
        :param request: the request
        :return: Nothing
        """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        print(session_id)
        if session_id is None:
            return False

        user_id = self.user_id_for_session_id(session_id)
        print(user_id)
        if not user_id:
            return False

        try:
            del self.user_id_by_session_id[session_id]
        except Exception:
            return False

        return True
