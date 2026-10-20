print("=" * 50)
print("        STUDENT LIST SYSTEM")
print("=" * 50)

students = []

for i in range(5):
    name = input(f"Enter Student {i+1} Name : ")
    students.append(name)

print("\nOriginal List")
print(students)

print("\nTotal Students")
print(len(students))

print("\nFirst Student")
print(students[0])

print("\nLast Student")
print(students[-1])

print("\nReverse List")
print(students[::-1])

print("\nSorted List")
students.sort()
print(students)

print("\nAdd New Student")
students.append(input("Enter New Student : "))
print(students)

print("\nInsert Student")
students.insert(1, input("Enter Student to Insert : "))
print(students)

print("\nRemove Student")
remove_name = input("Enter Student Name to Remove : ")

if remove_name in students:
    students.remove(remove_name)

print(students)

print("\nLoop")
for student in students:
    print(student)

print("\nTotal Students :", len(students))

print("=" * 50)