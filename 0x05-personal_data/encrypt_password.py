#!/usr/bin/env python3
"""
This module defines the hash_password function
"""
from bcrypt import hashpw, gensalt


def hash_password(password: str) -> bytes:
    """THis function hash a password using bcrypt method :
    - Converting password to array of bytes
    - Create a salt, a random data that will be added to the password
     before hashing
    - Hash the password in byte string and add the salt before
    """
    convert = password.encode('utf-8')
    salt = gensalt()
    hashed_password = hashpw(convert, salt)

    return hashed_password
