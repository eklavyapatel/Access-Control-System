#Objects
allUsers = {}
allGroups = []

#Object to store the name and password of a user
class User:
    def __init__(self,name,password):
        self.name = name
        self.password = password

    def add(self):
        if self.name in allUsers.keys():
            return ":::User already exists"
        else:
            allUsers[self.name] = self.password
            #print(allUsers[self.name])
            return ":::New user successfully created"
        # allUsers[self.name] = self.password
        # #print(allUsers[self.name])
        # return "New user successfully created"

class Group:
    def __init__(self, groupName):
        self.groupName = groupName
        self.users = []
        self.objects = []

    def makeMember(self,user_to_add):
        if user_to_add in self.users:
            return print("User already in group.")
        self.users.append(user_to_add)
        print(":::Successfully added User to Group.\n:::Current Users in "+self.groupName+":",self.users)

    def addObject(self, object_to_add):
        if object_to_add in self.objects:
            return print("Object already in group.")
        self.objects.append(object_to_add)
        print(":::Successfully added Object to Group.\n:::Current Objects in "+self.groupName+":", self.objects)

class Permission:
    def __init__ (self,usergroupname):
        self.usergroupname = usergroupname
        self.objectgroupname = ''
        self.access = []

    def addPermission(self,operation):
        if operation in self.access:
            return print(":::User Group already has access to " + operation + " on" + self.objectgroupname)
        self.access.append(operation)
        print(":::Permission to " + operation + self.objectgroupname + " successfully granted.")

    def printAccess():
        return
