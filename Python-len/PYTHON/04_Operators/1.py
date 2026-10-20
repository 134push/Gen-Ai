from secrets import choice
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)

## prcatice problems
print("======================")
num1 = int(input("enter the first number"))
num2 = int(input("enter the second number"))
choice = input("enter the choice of operations (+,-,*,/,%,**,//) : ")
match choice:
    case "+" : print("addition",num1+num2)
    case "-" : print("subtraction",num1-num2)
    case "*" : print("multiplication",num1*num2)
    case "/": print("division",num1/num2)
    case "%" : print("remainder",num1%num2)
    case "**" : print("power",num1**num2)    
    case "//" : print("floor division",num1//num2)
    case _ : print("invalid choice")
print("=======================")