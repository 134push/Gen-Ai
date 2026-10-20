with open("1.txt", "w") as file:
    file.write("Hello Pushpam")

with open("1.txt", "r") as file:
    print(file.read())

with open("1.txt", "a") as file:
    file.write("\nNew line")

with open("1.txt","r") as file:
    line = file.readlines()
print(line)        

with open("1.txt", "r") as file:
    for line in file:
        print(line.strip())