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
    #groupname = ""
    def __init__(self, groupName):
        self.groupName = groupName
        self.users = []

    # def __eq__ (self, other):
    #     return self.groupName == other.groupName

    def makeMember(self,user_to_add):
        self.users.append(user_to_add)
        print("Successfully added User to Group.\nCurrent Users:", self.users)
