#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import Base, User
from typing import Type


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memorized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Create a User
        :param email: the user email (requirement)
        :param hashed_password: the user password (requirement)
        :return: A User Object
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()

        return user

    def find_user_by(self, **kwargs) -> Type[User]:
        """ Find a User by its ID
        :param kwargs: arbitrary keyword arguments
        :return: The first row found in the users table
        """
        try:
            user = self._session.query(User).filter_by(**kwargs).first()
        except InvalidRequestError:
            raise InvalidRequestError

        if user is None:
            raise NoResultFound

        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """ Update a User by its ID
        :param user_id: the user ID
        :param kwargs: arbitrary keyword arguments
        :return: None
        """
        try:
            user = self.find_user_by(id=user_id)
            for name, value in kwargs.items():
                if hasattr(user, name):
                    setattr(user, name, value)
        except ValueError:
            raise ValueError

        self._session.commit()
