def apply_discount(price, discount_percent=0.05):
    if discount_percent < 0.6:
        new_price = price - (price * discount_percent)
        print(new_price)
    else:
        print("you got 50% Discount")
        new_price = price - (price * discount_percent)
        print(new_price)


apply_discount(1000, 0.10)
apply_discount(500)
