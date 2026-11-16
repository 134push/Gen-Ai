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

class laptop(Product):
    def __init__(self, name, price, category, percent,model):
        self.model = model 
        super().__init__(name, price, category, percent)
    def info(self):
        super().info()
        print(f"mobile no  is {self.model}\n")    
        
class Mobile(Product):
    def __init__(self, name, price, category, percent,cpu):
        self.cpu = cpu
        super().__init__(name, price, category, percent)
    def info(self):
        super().info()
        print(f"mobile no  is {self.cpu}\n") 

laptop = laptop("asus",79000,"laptop",5,"intel-i5")
laptop.info()
mobile = Mobile("iphone", 55000, "phone", 2,"17-pro")
mobile.info()