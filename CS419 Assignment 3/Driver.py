#Driver
from addUser import *
from authenticate import *
from addUserToGroup import *
from addObjectToGroup import *
from addAccess import *
from canAccess import *

print("\nInstructions on Running this Access Control System \n")
print("Valid Commands:\n")
print("\tAddUser [Username] [Password]\n")
print("\tAuthenticate [Username] [Password]\n")
print("\tAddUserToGroup [Username] [Group name]\n")
print("\tAddObjectToGroup [Object name] [Group name]\n")
print("\tAddAccess [Operation] [User Group name] [Object Group name]")
print("\t\tOR")
print("\tAddAccess [Operation] [User Group name]\n")
print("\tCanAccess [Operation] [Username] [Object name]")
print("\t\tOR")
print("\tCanAccess [Operation] [Username]\n")

while True:
    command = input("\nEnter Command: ")
    task = command.split()
    if (task[0] == "AddUser"):
        addUsers(task[1],task[2])
    elif(task[0] == "Authenticate"):
        authenticate(task[1],task[2])
    elif(task[0] == "AddUserToGroup"):
        addUserToGroup(task[1],task[2])
    elif(task[0] == "AddObjectToGroup"):
        addObjectToGroup(task[1],task[2])
    elif(task[0] == "AddAccess"):
        if (len(task) ==  3):
            addAccessNull(task[1],task[2])
        else:
            addAccess(task[1],task[2],task[3])
    elif(task[0] == "CanAccess"):
        if (len(task) ==  3):
            canAccessNull(task[1],task[2])
        else:
            canAccess(task[1],task[2],task[3])
    elif(task[0] == "Exit"):
        break
    else:
        print("Yo enter da correct command")