from Objects import *
# Add an object to an object group. If the group name does not exist, it is created. The object can be any string.
# The program should report
# - Success & list all the objects in that group
def addObjectToGroup(objectName,groupname):
    if any(x for x in allGroups if x.groupName == groupname):
        #take object and add user to the group
        for i in allGroups:
            if(i.groupName == groupname):
                i.addObject(objectName)
    else:
        #create group and add user
        newGroup = Group(groupname)
        allGroups.append(newGroup)
        #print(allGroups)
        newGroup.addObject(objectName)
