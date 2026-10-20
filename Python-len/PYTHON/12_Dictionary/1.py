print("=" * 50)
print("     STUDENT DICTIONARY SYSTEM")
print("=" * 50)

student = {}

student["name"] = input("Enter Name : ")
student["age"] = int(input("Enter Age : "))
student["branch"] = input("Enter Branch : ")
student["cgpa"] = float(input("Enter CGPA : "))
student["college"] = input("Enter College : ")

print("\nOriginal Dictionary")
print(student)

print("\nAccess Data")
print(student["name"])
print(student["cgpa"])

print("\nUpdate Age")
student["age"] += 1
print(student)

print("\nLength")
print(len(student))

print("\nKeys")
print(student.keys())

print("\nValues")
print(student.values())

print("\nItems")
print(student.items())

print("\nLoop")

for key, value in student.items():
    print(f"{key} : {value}")

print("\nMembership")
print("name" in student)

print("\nUsing get()")
print(student.get("salary"))

print("\nAdd Email")
student["email"] = "pushpam@gmail.com"

print(student)

print("\n" + "=" * 50)
print("     5 STUDENTS NESTED DICTIONARY")
print("=" * 50)

students = {
    "student1": {
        "id": 101,
        "name": "Rahul Sharma",
        "age": 20,
        "branch": "Computer Science",
        "cgpa": 8.8
    },
    "student2": {
        "id": 102,
        "name": "Priya Patel",
        "age": 21,
        "branch": "Information Technology",
        "cgpa": 9.2
    },
    "student3": {
        "id": 103,
        "name": "Amit Kumar",
        "age": 20,
        "branch": "Electronics",
        "cgpa": 7.9
    },
    "student4": {
        "id": 104,
        "name": "Neha Singh",
        "age": 22,
        "branch": "Mechanical",
        "cgpa": 8.5
    },
    "student5": {
        "id": 105,
        "name": "Pushpam Anand",
        "age": 21,
        "branch": "Artificial Intelligence",
        "cgpa": 9.6
    }
}

print("\nPrint Entire Nested Dictionary:")
print(students)

print("\nIterating through 5 Students:")
for student_id, details in students.items():
    print(f"\n{student_id.upper()}:")
    for key, value in details.items():
        print(f"  {key}: {value}")

print("\nAccess Specific Student Data (Student 5 Name):")
print(students["student5"]["name"])

print("=" * 50)