# Validate a user’s password by passing the username and password, both strings.
# The program should clearly report
# - Success
# - Failure: no such user
# - Failure: bad password
def Authenticate(user, password):
    for x in users:
        if x.user == user:
            if x.password == password:
                return "success"
            else:
                return "failure"
    return "failure"