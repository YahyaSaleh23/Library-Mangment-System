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
    try:
        is_email = validate_email(email)
        if is_email:
            return True
    except:
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

def input_loop(prompt,check,error,transform):
       while True:
                user_input = transform(input(prompt))
                if check(user_input):
                        return user_input
                else:
                        print(error)

def signup():
        first_name = input_loop("enter your first name: ",name_check,"that's not a real name", lambda user_input: user_input.strip().capitalize())
        last_name = input_loop("enter your last name: ",name_check,"that's not a real name", lambda user_input: user_input.strip().capitalize())
        name = f"{first_name} {last_name}" # combine first and last name together
        username = input_loop("enter your username: ",user_check,"your username less than 3", str.strip)
        password = input_loop("enter your password: ",password_check,"Your password is less than 8 characters", str.strip)
        hashed_password = md5(password.encode("utf-8")).hexdigest()
        email = input_loop("enter your email: ",email_check,"This email is not valid",str.strip)

        while True:
                    phone_number = input("enter your phone_number(optional): ").strip()
                    if len(phone_number) != 0:
                            is_real_number = phone_number_check(phone_number)
                            if is_real_number == 2:
                                print("Please enter real number and check your country  code")
                                continue
                            elif not is_real_number:
                                print("this number invalid")
                                continue
                            else:
                                    user = Client(name,username,hashed_password,email,phone_number).__dict__
                                    Library.add_user(user)
                                    break

                    # if user dont want enter his phone number
                    else: 
                            user = Client(name,username,hashed_password,email,phone_number="None").__dict__
                            Library.add_user(user)
                            break

def is_available(user,password):
      if len(user) != 0 and password == user['password'].iloc[0]:
            return True
      else:
            return False

def signin():
            while True:
                        user = input("enter your username or email: ").strip()
                        password = (md5(input("enter your password: ").rstrip().encode('utf-8')).hexdigest())
                        if '@' in user and user[0] != '@':
                                user = users[users['email'] == user]
                                if is_available(user, password):
                                        print("Welcome back!")
                                        return True
                                else:
                                        print("Invalid username or password. Please try again.")
                                        continue
                        else:
                                user = users[users['username'] == user]
                                if is_available(user, password):
                                        print("Welcome back!")
                                        return True
                                        
                                else:
                                        print("Invalid username or password. Please try again.")
                                        continue

