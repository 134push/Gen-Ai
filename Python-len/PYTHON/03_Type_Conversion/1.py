print("##1. Implicit Conversion")

age = "20"
age = int(age)
print(age + 5)

print("##2. Explicit Conversion")

a = 10
b = 5.5

c = a + b
print(c)
print(type(c))
c=int(c)
print(c)
print(type(c))

print("##3. String to Number")

price = "1500.50"
price = float(price)
print(price)
print(type(price))

print("##4. Boolean Values")
###0        → False
###Empty    → False
###Any value → True

a = 1
if a>0:
    print("true")
else:
    print("false")
print(bool(1))
print(bool(0))

print("##5. Complex Number")

a = 5
a = complex(a,8)
print(a)

