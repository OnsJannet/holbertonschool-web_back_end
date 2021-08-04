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
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False

    def authorization_header(self, request=None) -> str:
        ''' authorization header '''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        ''' current user '''
        return None
