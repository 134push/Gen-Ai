# fast track program

def hello():
    print("hello")
hello()

# function with parameters
def greet(name):
    print("Hello",name)
greet("python")  

# function with return value
def add(a, b):
    return a + b

result = add(10, 20)

print(result)

# function to functions

def gst(total):
    return total * 1.18
def discount(total):
    return total * 0.90
total = 1000
total = gst(total)
total = discount(total)

print(total)

# default parameter 

def greet(name="User"):
    print("Hello", name)
greet()
greet("Pushpam")

# keyword arguments

def student(name, age):
    print(name, age)
student(age=20, name="Pushpam")

#Arbitrary arguments (*args)

def add(*numbers):
    return sum(numbers)
result = add(10, 20, 30, 40, 50)
print(result)

#Arbitrary keyword arguments (**kwargs)

def student(**kwargs):
    print(kwargs)
student(name="Pushpam", age=20, city="New York", country="USA") 

# multiple return value 

def calculate(a, b):
    total = a + b
    difference = a - b

    return total, difference
result = calculate(10, 5)

print(result)    

# functions inside functions

def add(a, b):
    return a + b

def calculate():
    result = add(10, 20)
    print(result)

calculate()

# passing function as an argument 

def square(n):
    return n * n

def calculate(f, number):
    return f(number)

result = calculate(square, 5)

print(result)

# lambda functions

square = lambda n: n * n
print(square(5))

# map functions

numbers = [1, 2, 3, 4]
result = map(lambda x: x * 2, numbers)
print(list(result))

# filter 

numbers = [1, 2, 3, 4, 5, 6]
result = filter(lambda x: x % 2 == 0, numbers)
print(list(result))

numbers = [10, 15, 20, 25, 30, 35]
result = filter(lambda x: x>20,numbers)
print(list(result))

# reduce
from functools import reduce
numbers = [1, 2, 3, 4]
result = reduce(lambda a, b: a + b, numbers)
print(result)

# recursion

def count(n):
    if n == 0:
        return
    print(n)
    count(n - 1)
count(5)

