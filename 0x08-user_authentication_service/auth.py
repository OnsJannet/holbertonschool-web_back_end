#!/usr/bin/env python3
"""
AUTH
"""

import bcrypt
from db import DB
from user import Base, User
from uuid import uuid4
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    ''' hashes password'''
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    ''' Generate uuid
    '''
    UUID = uuid4()
    return str(UUID)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        ''' register user '''
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f'<{consult.email}> already exists.')
        except NoResultFound:
            hashed_password: str = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
        return user

    def valid_login(self, email: str, password: str) -> bool:
        ''' Validates loging cred '''
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        else:
            return bcrypt.checkpw(password=password.encode('utf-8'),
                                  hashed_password=user.hashed_password)
