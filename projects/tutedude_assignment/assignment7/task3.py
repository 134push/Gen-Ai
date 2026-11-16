class Product:
    def __init__(self, name, price, category, percent=5):
        self.name = name
        self.price = int(price)
        self.category = category
        self.percent = int(percent)
    def info(self):
        print(f"product name is {self.name}\nproduct price is {self.price}\nproduct category is {self.category}")
    def disscount(self):
        self.price = self.price - (self.price * (self.percent / 100))
        print(f"the discounted price is {self.price}")

class Electronicproduct(Product):
    def __init__(self, name, price, category, warrenty, percent=5):
        super().__init__(name, price, category, percent)
        self.warrenty = warrenty
    def info(self):
        super().info()
        print(f"product warrenty is {self.warrenty} years\n")

person1 = Product("milk", 120, "dairy")
person1.info()
laptop = Electronicproduct("Asus TUF", 55000, "Electronics", 2)
laptop.info()