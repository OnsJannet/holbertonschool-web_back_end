#!/usr/bin/env python3
"""
Basic authentication
"""

from api.v1.auth.auth import Auth
from flask import Flask, request
from base64 import b64decode


class BasicAuth(Auth):
    '''
    inherits from Auth
    '''

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
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
                                           base64_authorization_header:
                                           str) -> str:

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
