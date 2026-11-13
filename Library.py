from library_system import *
from Library_Managment import *
from hashlib import md5
is_login = False
is_running = True
while is_running:
    signup = input("Are you new here(Y/N)?").lower().strip()

    if  signup == "n":
         user = input("enter your username or email: ").strip()
         password = input("enter your password: ")
    elif signup == "y":
        first_name = input("enter your first name: ").capitalize().strip()
        if not name_check(first_name):
            print("that's not a real name")
            continue
        else:
                last_name = input("enter your last name: ").capitalize().strip()
                if not name_check(last_name):
                    print("that's not a real name")
                    continue
                else:
                        username = input("enter your username: ").strip()
                        if not user_check(username):
                                print("your username less then 3")
                                continue
                        else:
                            password = input("enter your password: ")
                            if not password_check(password):
                                    print("Your password is less than 8 characters")
                                    continue
                            else:
                                email = input("enter your email: ").strip()
                                if not email_check(email):
                                        print("This email is not valid")
                                else:                
                                    phone_number = input("enter your phone_number(optional): ").strip()
                                    if len(phone_number) != 0:
                                          phone_number_check(phone_number)
                                    else:
                                          pass