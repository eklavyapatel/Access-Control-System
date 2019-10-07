from Objects import *
# Test whether a user can perform a specified operation on an object. Optionally, an object may be NULL, in which case CanAccesschecks allows access if a user is part of a group for an operation on which no object group was defined.
# The program will check whether the user is allowed to perform the specified operation on the object. That means that there exists a valid access right for an operation where the user is in usergroupname and the object is in the corresponding objectgroupname.
# As with AddAccess, the program will accept two or three strings. If object is missing, it is considered null and the software allows access only if no object groups were defined for that {operation, usergroupname} set.
# Note that the parameters here are user names and object names, not user groups and object groups.
def canAccessNull(operation,user):
    for i in allUsers:
        if (i.name == user):
            for j in i.groups:
                for k in allPermissions:
                    if (j == k.usergroupname):
                        for l in k.access:
                            if (l == operation):
                                print ("::: Yes. "+user+" can "+operation)
                                return
                        #print("::: No. "+user+" can not "+operation)
                print("::: No. "+user+" can not "+operation)

def canAccess(operation,user,object_to_check):
    for i in allUsers:
        if (i.name == user):
            for j in i.groups:
                for k in allPermissions:
                    if (j == k.usergroupname):
                        for l in k.access:
                            if (l == operation):
                                for m in allGroups:
                                    for n in m.objects:
                                        if (object_to_check == n):
                                            print("::: Yes. "+user+" can "+operation +" "+object_to_check)
                                            return
                                    #print("::: No. "+user+" can not "+operation)
                print ("::: No. "+user+" can not "+operation+" "+object_to_check)