# Shopping Billing System

name = input("Enter your name: ")

print("\n")
print("========================================")
print("            SHOPPING BILL")
print("========================================")
print("\n")

item1 = input("Enter item 1 name: ")
price1 = float(input("Enter item 1 price: "))
qty1 = int(input("Enter item 1 quantity: "))
total1 = price1 * qty1

item2 = input("Enter item 2 name: ")
price2 = float(input("Enter item 2 price: "))
qty2 = int(input("Enter item 2 quantity: "))
total2 = price2 * qty2

item3 = input("Enter item 3 name: ")
price3 = float(input("Enter item 3 price: "))
qty3 = int(input("Enter item 3 quantity: "))
total3 = price3 * qty3

grand_total = total1 + total2 + total3


def gst_calculator(total):
    ans = input("Choose your GST: 5/12/18/28: ")

    if ans == "5":
        total = total * 1.05
    elif ans == "12":
        total = total * 1.12
    elif ans == "18":
        total = total * 1.18
    elif ans == "28":
        total = total * 1.28
    else:
        print("Invalid GST")

    return total


def discount_calculator(total):
    ans = input("Choose your discount: 5/10/15/20: ")

    if ans == "5":
        total = total * 0.95
    elif ans == "10":
        total = total * 0.90
    elif ans == "15":
        total = total * 0.85
    elif ans == "20":
        total = total * 0.80
    else:
        print("Invalid discount")

    return total


def payment(total):
    ans = input("Choose your payment method: online/offline: ")

    if ans.lower() == "online":
        print("Online payment")

        total = gst_calculator(total)
        total = discount_calculator(total)

        print("Total Price:", total)

    elif ans.lower() == "offline":
        total = total + 50

        print("Offline payment")

        total = gst_calculator(total)
        total = discount_calculator(total)

        print("Total Price:", total)
        print("You have to pay 50 Rs extra for offline payment")

    else:
        print("Invalid payment method")
        print("Total Price:", total)

    return total


print("\n")
print("========================================")
print("                 BILL")
print("========================================")
print("\n")

print("Customer Name:", name)
print("Item Name:", item1, item2, item3)
print("Item Price:", price1, price2, price3)
print("Item Quantity:", qty1, qty2, qty3)
print("Subtotal:", grand_total)

print("\n")
print("========================================")

final_amount = payment(grand_total)

print("========================================")
print("Final Amount:", final_amount)
print("========================================")

print("\nThank you for shopping with us!")