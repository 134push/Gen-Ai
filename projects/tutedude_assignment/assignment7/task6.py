class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price = int(price)
        self.category = category

    def __add__(self,other):
        return Product(self.name + " & " +other.name,self.price + other.price,self.category + " & " + other.category)

    def  __str__(self):
        return f"{self.name} with price {self.price} and category {self.category}"

person1 = Product("milk",120,"dairy")        
person2 = Product("tea",80,"dairy")

total = person1 + person2
print(total)
