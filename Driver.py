#Driver
from addUser import *
from authenticate import *
from addUserToGroup import *
from addObjectToGroup import *
from addAccess import *
from canAccess import *

while True:
    command = input("enter command\n")
    task = command.split()
    if (task[0] == "AddUser"):
        addUsers(task[1],task[2])
    elif(task[0] == "Authenticate"):
        print("OK")
        authenticate(task[1],task[2])
    elif(task[0] == "AddUserToGroup"):
        addUserToGroup(task[1],task[2])
    elif(task[0] == "AddObjectToGroup"):
        addObjectToGroup(task[1],task[2])
    elif(task[0] == "AddAccess"):
        addAccess(task[1],task[2],task[3])
    elif(task[0] == "CanAccess"):
        canAccess(task[1],task[2],task[3])
    elif(task[0] == "Exit"):
        break