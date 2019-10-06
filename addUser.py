from Objects import *

# Define a new user for the system along with the user’s password, both strings.
# The program should report an error if the user already exists.
def addUsers(user,password):
    if any(x for x in allUsers if x.name == user):
        return ":::User already exists"
    else:
        newUser = User(user,password)
        allUsers.append(newUser)
        print(":::New user successfully created.")

    