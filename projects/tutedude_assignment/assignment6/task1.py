numerator = int(input("enter your numerator : "))
denominator = int(input("enter your denominator : "))

try:
    result = numerator/denominator
    print(result)
except ValueError:
    print("pls enter a valid number : ")
except ZeroDivisionError:
    print("can not divide by zero : ")
else:
    print("result : ",result)
finally:
    print("operations completed : ")    