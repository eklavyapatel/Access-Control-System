# Test whether a user can perform a specified operation on an object. Optionally, an object may be NULL, in which case CanAccesschecks allows access if a user is part of a group for an operation on which no object group was defined.
# The program will check whether the user is allowed to perform the specified operation on the object. That means that there exists a valid access right for an operation where the user is in usergroupname and the object is in the corresponding objectgroupname.
# As with AddAccess, the program will accept two or three strings. If object is missing, it is considered null and the software allows access only if no object groups were defined for that {operation, usergroupname} set.
# Note that the parameters here are user names and object names, not user groups and object groups.
def canAccess(operation,user,object):
    return