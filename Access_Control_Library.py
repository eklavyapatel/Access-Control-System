
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

# Define a new user for the system along with the user’s password, both strings.
# The program should report an error if the user already exists.
def addUser(user,password):

# Validate a user’s password by passing the username and password, both strings.
# The program should clearly report
# - Success
# - Failure: no such user
# - Failure: bad password
def Authenticate(user, password):
    for x in users:
        if x.user == user:
            if x.password == password:
                return "success";
            else:
                return "failure";
return "failure";

# Add a user to a user group. If the group name does not exist, it is created. If a user does not exist, the function should return an error.
# The program should report
# - Success & list all the users in that group
# - Failure if the user does not exist
def addUserToGroup(user,groupname):

# Add an object to an object group. If the group name does not exist, it is created. The object can be any string.
# The program should report
# - Success & list all the objects in that group
def addObjectToGroup(objectName,groupName):

# Define an access right: a string that defines an access permission of a user group to an object group. The access permission can be an arbitrary string that makes sense to the service.
# The program will accept two or three strings. If objectgroupname is missing, it is considered null and the specified user group is simply permitted access to the operation regardless of the object (or an object may not make sense for that operation).
def addAccess(operation, userGroupName, objectGroupName):

# Test whether a user can perform a specified operation on an object. Optionally, an object may be NULL, in which case CanAccesschecks allows access if a user is part of a group for an operation on which no object group was defined.
# The program will check whether the user is allowed to perform the specified operation on the object. That means that there exists a valid access right for an operation where the user is in usergroupname and the object is in the corresponding objectgroupname.
# As with AddAccess, the program will accept two or three strings. If object is missing, it is considered null and the software allows access only if no object groups were defined for that {operation, usergroupname} set.
# Note that the parameters here are user names and object names, not user groups and object groups.
def canAccess(operation,user,object)

