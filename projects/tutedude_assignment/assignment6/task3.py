def check_age(age):
    if 120 < age or age < 1:
        raise ValueError("age must be between 1 to 120 : ")
    print("valid age : ")

try:
    age = int(input("enter your age : "))
    check_age(age)
except ValueError as e:
    print(e)                    
finally:
    print("done...")       