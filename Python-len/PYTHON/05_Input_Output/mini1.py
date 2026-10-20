
## █ □
import time
def loading():
    print("Loading", end="")
    time.sleep(0.9)
    print(".", end="")
    time.sleep(0.8)
    print(".", end="")
    time.sleep(0.3)
    print(".")
loading()
print("======================")
print("  == welcome to cvm ==")
print("======================")

print("enter your details")
name = input("Enter your name : ")
age = int(input("Enter your age : "))
gender = input("Enter your gender : ")
enrollment_no = input("Enter your enrollment number : ")
branch = input("Enter your branch : ")
semester = input("Enter your semester : ")
college = input("Enter your college : ")
no_subject = int(input("Enter number of subjects : "))
subject = []
for i in range(no_subject):
    subject.append(input(f"Enter subject {i+1} : "))
print("your id genrating please wait......")
import time 
spinner = ["|", "/", "-", "\\"]
for i in range(101):
    print("\r" + spinner[i % len(spinner)], end="")
    print(f"genrating id ... {i}%", end="")
    time.sleep(0.1 )
print("\n")    
print("\n")    
print("===============================")
print("       STUDENT ID CARD         ")
print("===============================")

print(f"Name        : {name}")
print(f"Enrollment  : {enrollment_no}")
print(f"Branch      : {branch}")
print(f"Semester    : {semester}")
print(f"College     : {college}")
print("subjects are : ", subject)

print(f"===============================")