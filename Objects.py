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
        self.objects = []
        self.access = []

    # def __eq__ (self, other):
    #     return self.groupName == other.groupName

    def makeMember(self,user_to_add):
        if user_to_add in self.users:
            return print("User already in group.")
        self.users.append(user_to_add)
        print("Successfully added User to Group.\nCurrent Users:", self.users)

    def addObject(self, object_to_add):
        if object_to_add in self.objects:
            return print("Object already in group.")
        self.objects.append(object_to_add)
        print("Successfully added Object to Group.\nCurrent Object:", self.objects)

    def addAccess(self, permission):
        if premission in self.access:
            return print("User Group already has permission for ",permission)
        self.access.append(premission)
        print("Permission successfully granted.\nCurrent Object:", self.access)