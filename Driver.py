#Driver
from addUser import *
from authenticate import *
from addUserToGroup import *
from addObjectToGroup import *
from addAccess import *
from canAccess import *

while True:
    command = input("\nEnter command: ")
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
        print("what the fuck")