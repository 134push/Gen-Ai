class Product:
    def __init__(self,name,price,category,percent = 5):
        self.name = name
        self.price = int(price)
        self.category = category
        self.percent = int(percent)

    def info(self):
        print(f"product name is {self.name}\nproduct price is {self.price} \nproduct category is {self.category} .\n ")    

    def disscount(self):
        self.price = self.price - (self.price*(self.percent/100))
        print(f"the discounted price is {self.price}")

person1 = Product("milk",120,"dairy")        
person2 = Product("tea",80,"dairy")

person1.info()
person1.disscount()

person2.info()
person2.disscount()