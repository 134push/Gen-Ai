class Product:
    def __init__(self,name,price,category,percent = 5):
        self.name = name
        self.__price = int(price)
        self.category = category
        self.percent = int(percent)

    def get_price(self):
        print(f"the price of the product is {self.__price}")
    def new_price(self,new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("the price is not updated ")        
person1 = Product("milk",120,"dairy")        

person1.get_price()

person1.new_price(500)
