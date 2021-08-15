#!/usr/bin/env python3
"""
AUTH
"""

import bcrypt


def _hash_password(password: str) -> str:
    ''' hashes password'''
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
