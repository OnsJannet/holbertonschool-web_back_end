#!/usr/bin/env python3
'''
Basic authentication
'''
from api.v1.auth.auth import Auth
from flask import Flask, request
from base64 import b64decode
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    '''
    BasicAuth: inherits from Auth
    '''
    def extract_base64_authorization_header(self,
                                            authorization_header: str
                                            ) -> str:
        '''
         returns the Base64 part of the Authorization
        '''
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith("Basic"):
            return None
        else:
            return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        '''
         returns returns the decoded value of a Base64 string
        '''
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            header_encode = base64_authorization_header.encode('utf-8')
            header_encode = b64decode(header_encode)
            header_encode = header_encode.decode('utf-8')
            return header_encode
        except BaseException:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        '''
         the user email and password from the Base64 decoded value.
        '''
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) is not str:
            return None, None
        if not (":") in decoded_base64_authorization_header:
            return None, None
        else:
            return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        '''
         the User instance based on his email and password.
        '''
        if user_email is None or user_pwd is None:
            return None
        if type(user_email) is not str:
            return None
        if type(user_pwd) is not str:
            return None
        try:
            users = User.search({'email': user_email})
        except BaseException:
            return None
        if len(users) == 0:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''
         overloads Auth and retrieves the User instance for a request.
        '''
        header = self.authorization_header(request)
        header = self.extract_base64_authorization_header(header)
        header = self.decode_base64_authorization_header(header)
        user = self.extract_user_credentials(header)
        return self.user_object_from_credentials(user[0], user[1])
