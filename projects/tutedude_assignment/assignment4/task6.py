import os

user = input("enter the file name : ")

if os.path.exists(user):
    with open(user, "r") as file:
        print(file.read())
else:
    print("file doesn't exist : ")
