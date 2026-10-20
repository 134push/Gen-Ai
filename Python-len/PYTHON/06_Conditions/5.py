# 5. Shop Discount System

amount = float(input("Enter total shopping amount (₹): "))

if amount >= 10000:
    discount_percent = 20
elif amount >= 5000:
    discount_percent = 10
else:
    discount_percent = 5

discount_amount = (amount * discount_percent) / 100
final_amount = amount - discount_amount

print(f"Discount: {discount_percent}%")
print(f"Discount Amount: ₹{discount_amount:.2f}")
print(f"Final Payable Amount: ₹{final_amount:.2f}")
