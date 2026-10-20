product_price = int(input("enter the amount of your product :"))

if product_price >= 2000:
    discount = product_price*0.15 + product_price*0.05 
    new_price = product_price-discount
    print(f"you got 15% discount and fixed tak 5%. your final price is = {new_price}")
elif 1500 <= product_price < 2000:
    discount = product_price*0.10 + product_price*0.05
    new_price = product_price-discount
    print(f"you got 10% discount and fixed tak 5%. your final price is = {new_price}")        
elif 1000 <= product_price < 1500:
    discount = product_price*0.07 + product_price*0.05
    new_price = product_price-discount
    print(f"you got 7% discount and fixed tak 5%. your final price is = {new_price}")
else:
    discount = product_price*0.05
    new_price = product_price-discount
    print(f"you got 0 discount and fixed tak 5%. your final price is = {product_price}")

