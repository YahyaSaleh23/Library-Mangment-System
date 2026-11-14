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
                        name = f"{first_name} {last_name}" # combine first and last name together
                        username = input("enter your username: ").strip()
                        if not user_check(username):
                                print("your username less than 3")
                                continue
                        else:
                            password = input("enter your password: ")
                            if not password_check(password):
                                    print("Your password is less than 8 characters")
                                    continue
                            else:
                                hashed_password = md5(password.encode("utf-8")).hexdigest()
                                email = input("enter your email: ").strip()
                                if not email_check(email):
                                        print("This email is not valid")
                                else:                
                                    phone_number = input("enter your phone_number(optional): ").strip()
                                    if len(phone_number) != 0:
                                          is_real_number = phone_number_check(phone_number)
                                          if is_real_number == 2:
                                                print("Please enter real number and check your country  code")
                                                continue
                                          elif not is_real_number:
                                                print("this number invalid")
                                          else:
                                                 register(name,username,hashed_password,email,phone_number)
                                                 is_login = True
                                    else:
                                          register(name,username,hashed_password,email)
                                          is_login = True