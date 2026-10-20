
def process_price(*a):

    discount1 = list(map(lambda x : x - (x * 0.10),a))
    print("after disscounting 10% : ",discount1)

    discount = list(filter(lambda x : x > 300,discount1))
    print("price above 300 are acceptable : ",discount)

process_price(100,500,900,50,750)    