#!/usr/bin/python3

from base_model import BaseModel

class User(BaseModel):
    """ User classes """
    email = ""
    password = ""
    first_name = ""
    last_name = ""