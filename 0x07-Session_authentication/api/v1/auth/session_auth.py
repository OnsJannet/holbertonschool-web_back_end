#!/usr/bin/env python3
'''
session authentication
'''
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    ''' enherits from Auth
    '''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        '''creates a Session ID for a user_id
        '''
        if user_id is None and type(user_id) is not str:
            return None

        ID = str(uuid4())
        self.user_id_by_session_id[ID] = user_id
        return ID
