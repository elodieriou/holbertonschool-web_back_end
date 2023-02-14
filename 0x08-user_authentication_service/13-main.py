#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth

email = 'test@test.com'
password = 'MyPwdOfBob'
auth = Auth()

auth.register_user(email, password)

session_id = auth.create_session(email)
print(session_id)

user = auth.get_user_from_session_id(session_id)
print(user.session_id)

auth.destroy_session(user.id)
print(user.session_id)
print(auth.destroy_session(23))
print(auth.destroy_session(None))

