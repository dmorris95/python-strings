#Task 1

command = ["help", "issue", "contact support", "feedback"]
'''
def input_parser(issue, com_list):
    low_iss = issue.lower()
    for c in com_list:
        if issue.find(c) != -1:
            if c == "help":
                print("You have asked for help, how can we help you today?")
            elif c == "issue":
                print("What issue are you dealing with?")
            elif c == "contact support":
                print("You have asked for customer support, someone will be in contact shortly.")
            elif c == "feedback":
                print("What feedback would you like to provide?")

print(command)
input_parser(input("Please type a command from the list above: "), command)
'''

#Task 2

def categorize_issue():
    isse = input("What is the issue you are dealing with? ").lower()
    if isse.find("performance") != -1:
        print("Someone from the support team will be in touch about the performance issue.")
    elif isse.find("error") != -1:
        print("Someone from the support team will be in touch in regards to the error you are having.")
    elif isse.find("login") != -1:
        print("Having trouble with the login, someone will be in touch to resolve this.")
    elif isse.find("connection") != -1:
        print("Having connection issues? We will resolve this as quick as we can.")

def input_parser(issue, com_list):
    low_iss = issue.lower()
    for c in com_list:
        if issue.find(c) != -1:
            if c == "help":
                print("You have asked for help, how can we help you today?")
            elif c == "issue":
                categorize_issue()
            elif c == "contact support":
                print("You have asked for customer support, someone will be in contact shortly.")
            elif c == "feedback":
                print("What feedback would you like to provide?")

print(command)
input_parser(input("Please type a command from the list above: "), command)
