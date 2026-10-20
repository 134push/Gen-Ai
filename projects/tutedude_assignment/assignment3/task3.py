
gst = lambda x: x + (x * 0.18)
discount = lambda x: x - (x * 0.05)

# Calculate GST on base price 100
gst_cal = gst(100)
print(f"Price after 18% GST: {gst_cal}")

# Apply 5% discount on GST price
final_price = discount(gst_cal)
print(f"Price after 5% Discount: {final_price}")
