#!/usr/bin/env python3

# Function that checks whether a username is a valid length.

# def validate_user(username, minlen):
#     if len(username) < minlen:
#         return False
#     if not username.isalnum():
#         return False
#     return True


# Function that checks whether a username is a valid length and raises exception

def validate_user(username, minlen):
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True

# Function that checks whether a username is a valid length and raises exception and assertion.

def validate_user(username, minlen):
    assert type(username) == str, "username must be a string"
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True