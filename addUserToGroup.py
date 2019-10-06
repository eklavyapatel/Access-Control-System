from Objects import *
# Add a user to a user group. If the group name does not exist, it is created. If a user does not exist, the function should return an error.
# The program should report
# - Success & list all the users in that group
# - Failure if the user does not exist
def addUserToGroup(user_to_add, groupname):
    if any(x for x in allUsers if x.name == user_to_add):
        #continue to add it to a group
        if any(x for x in allGroups if x.groupName == groupname):
            #take object and add user to the group
            for i in allGroups:
                if(i.groupName == groupname):
                    print(allUsers)
                    print("OK")
                    i.makeMember(user_to_add)
                    print(allUsers)
                    print("OK")
                    for i in allUsers:
                        print("OK")
                        if (i.name == user_to_add):
                            print("OK")
                            #add group to list
                            i.addToGroup(groupname)
        else:
            #create group and add user
            newGroup = Group(groupname)
            allGroups.append(newGroup)
            #print(allGroups)
            newGroup.makeMember(user_to_add)
            for i in allUsers:
                if (i.name == user_to_add):
                    #add group to list
                    i.addToGroup(groupname)
    else:
        print(":::FAILURE: User does not exist")
