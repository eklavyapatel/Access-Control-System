from Objects import *
# Define an access right: a string that defines an access permission of a user group to an object group. The access permission can be an arbitrary string that makes sense to the service.
# The program will accept two or three strings. If objectgroupname is missing, it is considered null and the specified user group is simply permitted access to the operation regardless of the object (or an object may not make sense for that operation).
def addAccess(operation, userGroupName, objectGroupName):
    return