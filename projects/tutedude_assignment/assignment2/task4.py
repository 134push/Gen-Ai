daily = [200,150,0,400,50,-1,300,0]
total_sales = []
for price in daily:
    if price == -1:
        break
    elif price == 0:
        continue
    else:
        final_price = 0
        print(price)
        final_price +=price
        total_sales.append(final_price)
print(f"the final total sales {sum(total_sales)}")