from Objects import *
# Validate a user’s password by passing the username and password, both strings.
# The program should clearly report
# - Success
# - Failure: no such user
# - Failure: bad password
def authenticate(user, password):
    if any(x for x in allUsers if x.name == user):
        for i in allUsers:
            if (i.name == user):
                if(i.password == password):
                    print(":::successfully authenticated")
                else:
                    print(":::Bad Password")
    else:
        print(":::Bad User")


    # if user in allUsers.keys():
    #     print(allUsers[user])
    #     if(allUsers[user] == password):
    #         print(":::successfully authenticated")
    #         #return "successfully authenticated"
    #     else:
    #         print(":::Bad Password")
    #         #return "Bad pasword"
    # else:
    #     print(":::Bad User")
        #return "Bad User"
    # for x in allUsers:
    #     if x.user == user:
    #         if x.password == password:
    #             return "success"
    #         else:
    #             return "failure"
    # return "failure"