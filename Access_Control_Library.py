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

    def makeMember(self,user_to_add):
        users = []
        users.append(user_to_add)
        return "User added to Group"


# Define a new user for the system along with the user’s password, both strings.
# The program should report an error if the user already exists.
def addUsers(user,password):
    newUser = User(user,password)
    print(newUser.add())

# Validate a user’s password by passing the username and password, both strings.
# The program should clearly report
# - Success
# - Failure: no such user
# - Failure: bad password
def Authenticate(user, password):
    print("OK")
    if user in allUsers.keys():
        print("OK")
        print(allUsers[user])
        if(allUsers[user] == password):
            print("successfully authenticated")
            #return "successfully authenticated"
        else:
            print("Bad Password")
            #return "Bad pasword"
    else:
        print("Bad User")
        #return "Bad User"
    # for x in allUsers:
    #     if x.user == user:
    #         if x.password == password:
    #             return "success"
    #         else:
    #             return "failure"
    # return "failure"
	
# Add a user to a user group. If the group name does not exist, it is created. If a user does not exist, the function should return an error.
# The program should report
# - Success & list all the users in that group
# - Failure if the user does not exist
def addUserToGroup(user_to_add, groupname):
    global allGroups
    if groupname in allGroups:
        #take object and add user to the group
        print(allGroups[allGroups.index(groupname)].makeMember(user_to_add))
    else:
        #create group and add user
        newGroup = Group(groupname)
        allGroups.append(newGroup)
        print(allGroups)
        newGroup.makeMember(user_to_add)
        print("Success")
    # global allUserGroups
    # if groupname not in allGroups:
    #     if user in allUsers.keys():
    #         allGroups = allGroups + (groupname,)
    #         allUserGroups = allUserGroups + (user, groupname)
    #         print ("Obect group object")
    #         print ("these are all objects in the group: %s" % (allGroups,))
    #     else:
    #         return "failure"

            

#def addUserToGroup(user,groupname):

# Add an object to an object group. If the group name does not exist, it is created. The object can be any string.
# The program should report
# - Success & list all the objects in that group
#def addObjectToGroup(objectName,groupName):

# Define an access right: a string that defines an access permission of a user group to an object group. The access permission can be an arbitrary string that makes sense to the service.
# The program will accept two or three strings. If objectgroupname is missing, it is considered null and the specified user group is simply permitted access to the operation regardless of the object (or an object may not make sense for that operation).
#def addAccess(operation, userGroupName, objectGroupName):

# Test whether a user can perform a specified operation on an object. Optionally, an object may be NULL, in which case CanAccesschecks allows access if a user is part of a group for an operation on which no object group was defined.
# The program will check whether the user is allowed to perform the specified operation on the object. That means that there exists a valid access right for an operation where the user is in usergroupname and the object is in the corresponding objectgroupname.
# As with AddAccess, the program will accept two or three strings. If object is missing, it is considered null and the software allows access only if no object groups were defined for that {operation, usergroupname} set.
# Note that the parameters here are user names and object names, not user groups and object groups.
#def canAccess(operation,user,object)


while True:
    command = input("enter command\n")
    task = command.split()
    if (task[0] == "AddUser"):
        addUsers(task[1],task[2])
    elif(task[0] == "Authenticate"):
        print("OK")
        Authenticate(task[1],task[2])
    elif(task[0] == "AddUserToGroup"):
        addUserToGroup(task[1],task[2])
    elif(task[0] == "AddObjectToGroup"):
        addObjectToGroup(task[1],task[2])
    elif(task[0] == "AddAccess"):
        addAccess(task[1],task[2],task[3])
    elif(task[0] == "CanAccess"):
        canAccess(task[1],task[2],task[3])
    elif(task[0] == "Exit"):
        break

    print (allUsers)