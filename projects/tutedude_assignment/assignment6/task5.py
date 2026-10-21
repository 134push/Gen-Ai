cart = []

while True:
    user1 = input("enter the number : ")
    if user1.strip().lower() == "q":
        break
    try:
        user = float(user1)
        if user < 0:
            raise ValueError("pls enter positive number only : ")
        cart.append(user)
    except ValueError as e:
        if "could not convert" in str(e):
            print("pls enter valid number : ")
        else:
            print(e)

print("the total item is : ", len(cart))
print("the total bill  is : ", sum(cart))