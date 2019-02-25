import re
import jwt

import datetime
from flask import jsonify, make_response


def validate_password(password):
    if re.match('[a-zA-Z0-9@#$&^%+=-]{6,}', password):
        return True
    return False


def is_alphabetic(data):
    if data.isalpha() == False:
        return False
    return True

def is_numbers(data):
    if re.match('^[0-9]*$', data) is None:
        return False
    return True
def is_string(data):
    if not isinstance(data, str):
        return False
    return True
def is_integer(data):
    if not isinstance(data, int):
        return False
    return True

def email_type(email):
    if re.match(r"(^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z0-9-.]+$)", email):
        return True
    return False

def spaces(data, inputs):
    for key, value in data.items():
        if key in inputs and not value.strip():
            return False
    return True
