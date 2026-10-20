user = input("enter your file name : ")

try:
    with open(user,"r") as file:
        for i in range(3):
            line = file.readline()
            if line == "":
                break
            print(line,end="")    
except FileNotFoundError:
    print("file not exist : ")
except PermissionError:
    print("permission denied : ")
finally:
    print("operations completed : ")            