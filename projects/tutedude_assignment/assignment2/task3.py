orders = [1200,2500,800,1750,3000]
new_orders = []
disscount_0 = []

print("----menu----")
print("1.add order to a running list : ")
print("2.show all orders and totals after applying discounts : ")
print("3.quit : ")
while True:
    user = input("enter your option : ")
    if user == "1":
        add_item = int(input("enter the new order amount :"))
        orders.append(add_item)
    elif user == "2":
        new_orders = []
        disscount_0 = []
        for i,product_price in enumerate(orders):
            if product_price >= 2000:
                discount = product_price*0.15 
                tax = product_price*0.05
                new_price = product_price-discount+tax
                new_orders.append(new_price)
                print(f"{i} -> you got 15% discount and fixed tak 5%. your final price is = {new_price}")
            elif 1500 <= product_price < 2000:
                discount = product_price*0.10
                tax = product_price*0.05
                new_price = product_price-discount+tax
                new_orders.append(new_price)               
                print(f"{i} -> you got 10% discount and fixed tak 5%. your final price is = {new_price}")        
            elif 1000 <= product_price < 1500:
                discount = product_price*0.07
                tax = product_price*0.05
                new_price = product_price-discount+tax
                new_orders.append(new_price)
                print(f"{i} -> you got 7% discount and fixed tak 5%. your final price is = {new_price}")
            else:
                tax = product_price*0.05
                product_price = product_price + tax
                new_orders.append(product_price)
                print(f"{i} -> you got 0 discount and fixed tak 5%. your final price is = {product_price}")
                disscount_0.append(i)    
        print(f"\ntotal amount is = {sum(new_orders)}")         
    elif user == "3" or user == "q":
        print("Exiting...")
        break
    else:
        print("invalid input : ")
        break
