#!/usr/bin/env python3
""" Module of Session Expiration Authentication
"""
from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """Class SessionExpAuth defines the followings methods:
        - create_session
        - user_id_for_session_id
    """

    def __init__(self):
        """ Overload for assign an instance attribute session_duration
        """
        session_duration: str = getenv("SESSION_DURATION")
        try:
            session_duration: int = int(session_duration)
        except Exception:
            session_duration = 0

        self.session_duration = session_duration

    def create_session(self, user_id: str = None) -> str:
        """ Overload for update user_id and created_at when the session
        is created
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        session_dictionary = {
            'user_id': user_id,
            'created_at': datetime.now()
        }

        SessionAuth.user_id_by_session_id[session_id] = session_dictionary

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Overload to check created_at and session duration to return
        the user ID
        """
        if session_id is None:
            return None

        session_dictionary = SessionAuth.user_id_by_session_id.get(session_id)
        if session_dictionary is None:
            return None

        created_at = session_dictionary.get('created_at')
        if created_at is None:
            return None

        if self.session_duration <= 0:
            return session_dictionary.get('user_id')

        session_duration = timedelta(seconds=self.session_duration)
        delay_expiration = created_at + session_duration
        if delay_expiration < datetime.now():
            return None

        return session_dictionary.get('user_id')
