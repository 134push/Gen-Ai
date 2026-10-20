def apply_discount(price,percent):
    discount = price - (price*(percent/100))
    return discount 

def flat_discount(price):
    discount = price - 50
    return discount
