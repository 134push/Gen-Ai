discount_pct = float(input("enter the discount percentage : "))
discount_rate = discount_pct / 100

price = {
    "mouse": 500,
    "keyboard": 800,
    "monitor": 7000,
    "pendrive": 400,
    "camera": 5000,
}

with open("discount_report.txt", "w") as file:
    for item, original_price in price.items():
        discounted_price = original_price - (original_price * discount_rate)
        file.write(f"{item} : {discounted_price}\n")


with open("discount_report.txt", "r") as file:
    print(file.read())
