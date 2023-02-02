#!/usr/bin/env python3
"""
This module defines the hash_password function
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """This function hash a password using bcrypt method :
    - Converting password to array of bytes
    - Create a salt, a random data that will be added to the password
     before hashing
    - Hash the password in byte string and add the salt before
    Return the hashed password
    """

    convert = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(convert, salt)

    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """This function checks if the password is valid :
    - Convert en byte the password
    - Check if the password in bytes is in hashed password
    Return True if it is the great password, False otherwise
    """

    convert = password.encode('utf-8')
    check = bcrypt.checkpw(convert, hashed_password)

    return check
