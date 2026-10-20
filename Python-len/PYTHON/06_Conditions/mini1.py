## Student Management System Menu
import time


def view_marks():
    print("--- View Marks ---")
    maths = float(input("Enter Maths marks: "))
    science = float(input("Enter Science marks: "))
    english = float(input("Enter English marks: "))
    print(f"Maths: {maths}")
    print(f"Science: {science}")
    print(f"English: {english}")


def find_avg_marks():
    print("--- Find Average Marks ---")
    maths = float(input("Enter Maths marks: "))
    science = float(input("Enter Science marks: "))
    english = float(input("Enter English marks: "))
    avg = (maths + science + english) / 3
    print(f"Average Marks: {avg:.2f}")


def find_top_scorer():
    print("--- Find Top Scorer ---")
    maths = float(input("Enter Maths marks: "))
    science = float(input("Enter Science marks: "))
    english = float(input("Enter English marks: "))

    if maths >= science and maths >= english:
        top_subject = "Maths"
        top_marks = maths
    elif science >= maths and science >= english:
        top_subject = "Science"
        top_marks = science
    else:
        top_subject = "English"
        top_marks = english

    print(f"Top Subject: {top_subject} with {top_marks} marks")


def find_weak_subject():
    print("--- Find Weak Subject ---")
    maths = float(input("Enter Maths marks: "))
    science = float(input("Enter Science marks: "))
    english = float(input("Enter English marks: "))

    if maths <= science and maths <= english:
        weak_subject = "Maths"
        weak_marks = maths
    elif science <= maths and science <= english:
        weak_subject = "Science"
        weak_marks = science
    else:
        weak_subject = "English"
        weak_marks = english

    print(f"Weakest Subject: {weak_subject} with {weak_marks} marks")


def exit_system():
    print("Exiting system. Goodbye!")


print("===========================")
print(" Student Management System ")
print("===========================")
print("loading.", end=" ")
print(".", end=" ")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print("\n")
print("1. view marks")
print("2. find avg marks")
print("3. find top scorer")
print("4. find weak subject")
print("5. Exit")
print("========================")

choice = input("Enter your choice: ")
print("good ! we connected you to the server now you can use the system....")
spinner = ["|", "/", "-", "\\"]

print("Downloading File...")

for i in range(101):
    filled = "█" * (i // 2)
    empty = "░" * (50 - (i // 2))

    spin = spinner[i % len(spinner)]
    print(f"\r{spin} [{filled}{empty}] {i}%", end="", flush=True)
    time.sleep(0.05)
print("\n")
print("you connceted ")
## Match case
match choice:
    case "1":
        print("view marks")
        view_marks()
    case "2":
        print("find avg marks")
        find_avg_marks()
    case "3":
        print("find top scorer")
        find_top_scorer()
    case "4":
        print("find weak subject")
        find_weak_subject()
    case "5":
        print("Exit")
        exit_system()
    case _:
        print("Invalid Choice")
