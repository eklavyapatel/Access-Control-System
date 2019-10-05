#Driver
from addUser import *
# allUsers = {}

# #Object to store the name and password of a user
# class User:
#     def __init__(self,name,password):
#         self.name = name
#         self.password = password

#     def add(self):
#         if self.name in allUsers.keys():
#             return "User already exists"
#         else:
#             allUsers[self.name] = self.password
#             #print(allUsers[self.name])
#             return "New user successfully created"
#         # allUsers[self.name] = self.password
#         # #print(allUsers[self.name])
#         # return "New user successfully created"

while True:
    command = input("enter command\n")
    task = command.split()
    if (task[0] == "AddUser"):
        addUsers(task[1],task[2])
    elif(task[0] == "Authenticate"):
        print("OK")
        Authenticate(task[1],task[2])
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