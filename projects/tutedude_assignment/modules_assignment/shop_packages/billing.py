from shop_packages import discount

def Calculate_total(price,percent):
    discount1 = discount.apply_discount(price,percent)
    discount2 = discount.flat_discount(discount1)
    return discount2

def apply_tax(amount):
    tax = amount - (amount * 0.05)
    return tax