total_sales = 0
max_value = 0
low_value = 0
avg = 0

with open("sales_data.txt", "r") as file:
    for line in file:
        line = int(line)
        if line:  
            total_sales += line

        if max_value < line:
            max_value = line
print("Total Sales:", total_sales)  
print("max value :",max_value)

with open("sales_data.txt", "r") as file:
    low_value = max_value
    for line in file:
        line = int(line)
        if low_value > line:
            low_value = line

print("low value :",low_value)
with open("sales_data.txt", "r") as file:
    for line in file:
        read = file.readlines()
        avg = total_sales/len(read)


print("avg value :",avg)
