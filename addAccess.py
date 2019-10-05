from Objects import *
# Define an access right: a string that defines an access permission of a user group to an object group. The access permission can be an arbitrary string that makes sense to the service.
# The program will accept two or three strings. If objectgroupname is missing, it is considered null and the specified user group is simply permitted access to the operation regardless of the object (or an object may not make sense for that operation).
def addAccess(operation, userGroupName):
    if any(x for x in allGroups if x.groupName == groupname):
        #take object and add user to the group
        for i in allGroups:
            if(i.groupName == groupname):
                i.addAccess(operation)
    else:
        #group doesnt exist
        print("YOU SUCK. Group doesn not exist.")

def addAccessNull(operation, userGroupName, objectGroupName):
    return