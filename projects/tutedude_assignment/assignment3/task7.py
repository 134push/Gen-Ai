
price_list = [100,500,900,50,750]

def add_price(price_list,price):
    print("before : ",price_list)
    price_list.append(price)
    print("after : ",price_list)

def avg_price(price_list):
    avg = sum(price_list)/len(price_list)
    print("the avg of prices : ",avg)    

def max_price(price_list):
    max_price = max(price_list)
    print("max price in the price_list : ",max_price)

print("---menu---")
print("1.add price")
print("2.avg price")
print("3.max price")
print("4.exit")

user = input("enter your choice : ")
print("the original list is : ",price_list)
if user == "1":
    add_price(price_list,120)    
elif user == "2":
    avg_price(price_list)
elif user == "3":   
    max_price(price_list)
elif user == "4":
    print("exit....")
else:
    print("invalid choice : ")
