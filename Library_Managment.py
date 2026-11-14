from library_system import *
from pandas import concat , read_json
from email_validator import validate_email
from phonenumbers import parse, is_valid_number
from hashlib import md5
users = read_json("users.json")

def name_check(name):
    if len(name) >= 2:
        return True
    else:
        return False


def user_check(username):
    if len(username) >= 3:
        return True
    else:
        return False


def password_check(password):
    if len(password) >=8:
        return True
    else: 
        return False

def email_check(email):
    is_email = validate_email(email)
    if is_email:
        return True
    else:
        return False

def phone_number_check(phone_number):
        try:
            if '+' in phone_number[0]:
                parse_number = parse(phone_number)
            else:
                    phone_number = f"+{phone_number}"
                    parse_number = parse(phone_number)
            if is_valid_number(parse_number):
                return True
            else:
                return False
        except:
             # in case the user inputs an invalid country code or an invalid number or phone_number
             return 2 

def register(name, username, password, email, phone_number=None):

        if phone_number == None:
             Client(name,username,password,email,phone_number="None")
        else: 
             Client(name,username,password,email,phone_number)