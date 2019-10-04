# Define a new user for the system along with the user’s password, both strings.
# The program should report an error if the user already exists.
def addUsers(user,password):
    newUser = User(user,password)
    print(newUser.add())