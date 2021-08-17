#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User


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
    def _session(self):
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        '''returns a User object that should save the user to the database.
        '''
        user = User(email=email, hashed_password=hashed_password)
        session = self._session
        session.add(user)
        session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        '''returns the first row found in the users table.
        '''
        if not kwargs:
            raise InvalidRequestError

        data = User.__table__.columns.keys()
        for key in kwargs.keys():
            if key not in data:
                raise InvalidRequestError

        session = self._session
        user = session.query(User).filter_by(**kwargs).first()
        if not user:
            raise NoResultFound
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        ''' returns None nad updates user
        '''
        if not kwargs:
            return None

        session = self._session
        user = self.find_user_by(id=user_id)

        data = User.__table__.columns.keys()
        for key in kwargs.keys():
            if key not in data:
                raise ValueError

        for key, value in kwargs.items():
            setattr(user, key, value)
        self._session.commit()
