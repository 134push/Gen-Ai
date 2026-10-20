catlog = [
    ("milk", 56, "dariy product"),
    ("choclates", 120, "packet food"),
    ("shoes", 869, "clothes"),
    ("notebook", 56, "school product"),
    ("light", 450, "home product"),
    ("tea", 40, "dariy product")
]

print("Catalog:")
for item in catlog:
    print(item)

categories_to_product = {
    "dariy product" : ["milk","tea"],
    "packet food" : ["chocaltes"],
    "clothes" : ["shoes"],
    "school product" : ["notebook"],
    "home product" : ["light"]
}    

for key,value in categories_to_product.items():
    print(f"{key} has a  {len(value)} no of products and the product is {value}")