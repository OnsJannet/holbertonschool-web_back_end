#!/usr/bin/env python3
'''
session authentication
'''
from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    ''' enherits from Auth
    '''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        '''creates a Session ID for a user_id
        '''
        if user_id is None or type(user_id) is not str:
            return None

        ID = str(uuid4())
        self.user_id_by_session_id[ID] = user_id
        return ID

    def user_id_for_session_id(self, session_id: str = None) -> str:
        '''returns a User ID based on a Session ID
        '''
        if session_id is None or type(session_id) is not str:
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        ''' returns a User instance based on a cookie value
        '''
        session_cookies = self.session_cookie(request)
        if session_cookies is None:
            return None
        user_id = self.user_id_for_session_id(session_cookies)
        return User.get(user_id)

    def destroy_session(self, request=None):
        ''' deletes the user session / logout
        '''
        if request is None:
            return False
        session_cookies = self.session_cookie(request)
        if not session_cookies:
            return False
        user_id = self.user_id_for_session_id(session_cookies)
        if not user_id:
            return False
        del self.user_id_by_session_id[session_cookies]
        return True
