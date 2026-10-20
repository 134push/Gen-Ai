products = [100, 250, 400, 1200, 50]

# 1. Calculate 18% GST on all products using map
gst_prices = list(map(lambda x: x + (x * 0.18), products))
print(f"Prices after 18% GST: {gst_prices}")

# 2. Apply 5% discount on the GST prices using map
final_prices = list(map(lambda x: x - (x * 0.05), gst_prices))
print(f"Prices after 5% Discount: {final_prices}")

