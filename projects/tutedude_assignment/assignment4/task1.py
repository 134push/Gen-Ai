sales = ['1200','450','980','1500','3000']

with open("sales_data.txt","w") as file:
    file.writelines("\n".join(sales))

with open("sales_data.txt","r") as file:
    new_read = file.read()
    print(new_read)