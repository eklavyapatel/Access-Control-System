from Objects import *
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