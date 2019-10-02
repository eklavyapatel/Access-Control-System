
#Object to store the name and password of a user
class User:
    def __init__(self,name,password):
        self.name = name
        self.password = password



# p1 = User("myname", "mypassword")

# print(p1.name)
# print(p1.password)

class Group:
    def __init__(self,)


def Authenticate(user, password):
    for x in users:
        if x.user == user:
            if x.password == password:
                return "success";
            else:
                return "failure";
return "failure";

def AddAccess(operation, userGroupName, objectGroupName):
