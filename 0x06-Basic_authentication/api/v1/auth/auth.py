#!/usr/bin/env python3
"""
manages the API authentication
"""
from flask import Flask, request
from typing import List, TypeVar


class Auth():
    '''
    a class that manages the API authentication
    '''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        ''' require authorithation '''
        return False

    def authorization_header(self, request=None) -> str:
        ''' authorization header '''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        ''' current user '''
        return None
