#!/usr/bin/env python3
""" Module of Session Database Authentication
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import timedelta, datetime


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
        user_session.save()

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Overload to return the User ID by requesting UserSession in the
        database based on session_id
        """
        if session_id is None:
            return None

        user_session = UserSession.search({'session_id': session_id})
        if not user_session:
            return None

        user = user_session[0]
        user_id = user.user_id

        created_at = user.created_at
        if created_at is None:
            return None

        session_duration = timedelta(seconds=self.session_duration)
        delay_expiration = created_at + session_duration

        if delay_expiration < datetime.utcnow():
            return None

        return user_id

    def destroy_session(self, request=None) -> bool:
        """ Overload to destroy the UserSession based on the session ID
        """

        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_id = self.user_id_for_session_id(session_id)
        if not user_id:
            return False

        user_session = UserSession.search(
            {'session_id': session_id}
        )

        user = user_session[0]
        user.remove()
        user.save_to_file()

        return True
