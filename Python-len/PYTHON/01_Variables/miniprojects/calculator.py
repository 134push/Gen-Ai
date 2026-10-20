import time

print("====================")
print("     CALCULATOR     ")
print("====================")

input1 = int(input("Enter the first number : "))
input2 = int(input("Enter the second number : "))

print("Sum :", input1 + input2)
print("Difference :", input1 - input2)
print("Product :", input1 * input2) 
print("Division :", input1 / input2)
print("Floor Division :", input1 // input2)
print("Modulus :", input1 % input2)
print("Exponentiation :", input1 ** input2)

print("====================")
print("     student os     ")
print("====================")

today_study_hours = int(input("Enter the current study hours you have : "))
target_study_hours = int(input("Enter the daily study hours you have : "))

study_hours_remaining = target_study_hours - today_study_hours
print("Study hours remaining :", study_hours_remaining)

print("=========================")
print("     security system     ")
print("=========================")
