#!/usr/bin/env python3
""" Module of Session Database Authentication
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """ Class SessionDBAuth defines the followings methods:
        - create_session
        - user_id_for_session_id
        - destroy_session
    """

    def create_session(self, user_id: str = None) -> str:
        """ Overload for create and stores new instance of UserSession
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        user_session = UserSession(user_id=user_id,
                                   session_id=session_id)
        user_session.save_to_file()

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Overload to return the User ID by requesting UserSession in the
        database based on session_id
        """
        if session_id is None:
            return None

        # Retrieve all object from db_UserSession.json
        UserSession.load_from_file()

        # Search the UserSession based on the session_id
        user_session = UserSession.search(
            {'session_id': session_id}
        )

        # Select the first user (only one user store)
        user = user_session[0]

        # Retrieve the user_id
        user_id = user.user_id

        return user_id

    def destroy_session(self, request=None) -> bool:
        """ Overload to destroy the UserSession based on the session ID
        """

        if request is None:
            return False

        # Retrieve session_id from the request cookie
        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        # Retrieve user_id from session_id
        user_id = self.user_id_for_session_id(session_id)
        if not user_id:
            return False

        # Search the user from session_id
        user_session = UserSession.search(
            {'session_id': session_id}
        )

        user = user_session[0]
        user.remove()
        user.save_to_file()

        return True
