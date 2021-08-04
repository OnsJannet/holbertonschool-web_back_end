#!/usr/bin/env python3
"""
Basic authentication
"""

from api.v1.auth.auth import Auth
from flask import Flask, request


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
