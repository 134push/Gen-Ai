orders = [1200,2500,800,1750,3000]
disscount_0 = []
for i,product_price in enumerate(orders):
    if product_price >= 2000:
        discount = product_price*0.15 
        tax = product_price*0.05
        new_price = product_price-discount+tax
        print(f"{i} -> you got 15% discount and fixed tak 5%. your final price is = {new_price}")
    elif 1500 <= product_price < 2000:
        discount = product_price*0.10
        tax = product_price*0.05
        new_price = product_price-discount+tax
        print(f"{i} -> you got 10% discount and fixed tak 5%. your final price is = {new_price}")        
    elif 1000 <= product_price < 1500:
        discount = product_price*0.07
        tax = product_price*0.05
        new_price = product_price-discount+tax
        print(f"{i} -> you got 7% discount and fixed tak 5%. your final price is = {new_price}")
    else:
        tax = product_price*0.05
        product_price = product_price + tax
        print(f"{i} -> you got 0 discount and fixed tak 5%. your final price is = {product_price}")
        disscount_0.append(i)

print(f"total product that dosent get disscount = {len(disscount_0)}")        


