prices = [120, 350, 'abc', 500, -200, 800]
total = 0

for item in prices:
    try:
        price = int(item)
        if price < 0:
            raise ValueError("Negative price not allowed")
        total += price
    except (TypeError, ValueError) as e:
        print("Skipped:", item, "-", e)
print("Total:", total)