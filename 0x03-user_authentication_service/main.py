#!/usr/bin/env python3
"""
Main file
"""
import requests


def register_user(email: str, password: str) -> None:
    """
    Test for register a user with the given email and password
    """
    resp = requests.post('http://127.0.0.1:5000/users',
                         data={'email': email, 'password': password})
    if resp.status_code == 200:
        assert (resp.json() == {"email": email, "message": "user created"})
    else:
        assert(resp.status_code == 400)
        assert (resp.json() == {"message": "email already registered"})
