#Task 1

def valid_name():
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    while len(first_name) < 2:
        print("Your first name is not enough characters.")
        first_name = input("Enter your first name: ")
    while len(last_name) < 2:
        print("Your last name is not enough characters.")
        last_name = input("Enter your last name: ")

valid_name()


#Task 2

def pass_complex():
    password = input("Please enter a passowrd: ")
    while len(password) < 8 or password.islower() == True or password.isupper() == True or password.isalpha() == True:
        print("Your password must be at least 8 characters, contain at least one upper and lowercase letter and at least one number.")
        password = input("Please enter your password: ")

pass_complex()


#Task 3

def email_checker():
    email = input("Please enter your email address: ")
    web_check = ""
    check = False
    if email.find("@") != -1:
        web_check = email[email.find("@"):]
        if web_check.startswith("@.") == True:
            check = False
        else:
            check = True
    while email.endswith(".com") == False and email.endswith(".edu") == False and email.endswith(".org") or email.find("@") == -1 or check == False:
        if email.find("@") != -1:
            web_check = email[email.find("@"):]
            if web_check.startswith("@.") == True:
                check = False
            else:
                check = True
        print("Your email must end with .com, .org or .edu, and contain @")
        email = input("Please enter your email: ")

email_checker()