price_dict = {"milk" : 45 ,"choclates" : 123,"hair oil" : 96,"shoes" : 869,"light" : 450 ,"suger" : 389}

# add a new products

price_dict["notebook"] = 56
print(price_dict)

# update a price of the product 

price_dict["choclates"] = 120
print(price_dict)

# delete a key from dictionary

del price_dict["milk"]
print(price_dict)


## avg price of all products
sum_product = 0

for key,value in price_dict.items():
    sum_product += value

print(sum_product)   

avg_price = sum_product / len(price_dict)
print(avg_price)
