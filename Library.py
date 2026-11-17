from library_system import *
from Library_Managment import *
from hashlib import md5

is_login = False
is_running = True

while is_running:
    if not is_login:
        is_sign = input("Are you new here(Y/N)?").lower().strip()

        if  is_sign == "n":
            signin()
            is_login = True
        elif is_sign == "y":
            signup()
            is_login = True
    else:
        user_interface()