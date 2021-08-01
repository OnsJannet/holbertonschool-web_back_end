#!/usr/bin/env python3
"""
password hashing
"""
import bcrypt


def hash_password(password: str) -> bytes:
    '''
    expects one string argument name password and returns a salted
    hashed password, which is a byte string.
    '''
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''
    returns a boolean.
    '''
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        return True
    else:
        return False
