class inventory:

    products = []

    def __init__(self, product=0):
        self.product = int(product)

    def add_product(self):
        self.products.append(self.product)

    def remove_product(self):
        self.products.remove(self.product)

    def get_total_value(self):
        return sum(self.products)

    def show_all_products(self):
        print(self.products)


class store(inventory):
    def __init__(self, store_name, product=0):
        super().__init__(product)
        self.store_name = store_name

    def add_new_product(self):
        self.product = int(input("enter the product price: "))
        super().add_product()

    def show_summary(self):
        print(f"store name is {self.store_name}")
        print(f"total no of products is {len(self.products)}")
        print(f"the sum of all product is {super().get_total_value()}")


my_store = store("Pushpam Store")

for i in range(3):
    my_store.add_new_product()

my_store.show_summary()