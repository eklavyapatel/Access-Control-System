#Objects
allUsers = {}
allGroups = []
# allGroups = ()
# allUserGroups = ()


#Object to store the name and password of a user
class User:
    def __init__(self,name,password):
        self.name = name
        self.password = password

    def add(self):
        if self.name in allUsers.keys():
            return "User already exists"
        else:
            allUsers[self.name] = self.password
            #print(allUsers[self.name])
            return "New user successfully created"
        # allUsers[self.name] = self.password
        # #print(allUsers[self.name])
        # return "New user successfully created"

class Group:
    
    groupname = ""
    
    def __init__(self, groupname):
        self.groupname = groupname

    def __eq__ (self, other):
        return self.groupname == other.groupname

    def makeMember(self,user_to_add):
        users = []
        users.append(user_to_add)
        return "User added to Group"
