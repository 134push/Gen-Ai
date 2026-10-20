with open("sales_data.txt","a") as file:
    file.write("\n5000\n2500\n1700")

with open("sales_data.txt", "r") as file:
    read = file.readlines()
    print(read)
    len_file = len(read)
    print(len_file)