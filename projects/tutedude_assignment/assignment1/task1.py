products = ["milk","choclates","chess","suger","tea","brushes","shoes","notebook","women tshirt"]

sample_product = ("milk",64,"dari_product")

print(f"second product from product_list is {products[2]} and last product from product_list is {products[4]} ")

## add products into list
products.append("oil")
products.append("shampoo")

print(products)

## convert the tuple into list then update and again convert into tuple

sample_product = list(sample_product)

sample_product[1] = 56

sample_product = tuple(sample_product)

print(sample_product)