with open("product.txt","w+") as file:
    for i in range(3):
        name = input("enter your product name : ")
        price = int(input("enter your product price : "))
        file.write(f"{name} : {price}\n")
    file.seek(0)
    read = file.read()
    print(read)