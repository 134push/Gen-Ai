with open("sales_data.txt","r") as file:
    read = file.read()
    print(read)

# reading the first line only
open1 = open("sales_data.txt","r")
print(open1.readline())
open1.close()

with open("sales_data.txt", "r") as file:
    read = [line.strip() for line in file.readlines()]
    print(read)




    
    
