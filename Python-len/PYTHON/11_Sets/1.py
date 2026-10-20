print("=" * 50)
print("        SET PRACTICE SYSTEM")
print("=" * 50)

subjects = {
    "Python",
    "C",
    "Flask",
    "Python",
    "Git",
    "SQLite"
}

print("\nOriginal Set")
print(subjects)

print("\nLength")
print(len(subjects))

print("\nAdd Subject")
subjects.add("AI")
print(subjects)

print("\nUpdate Subjects")
subjects.update(["Cloud", "Docker"])
print(subjects)

print("\nRemove Subject")
subjects.remove("C")
print(subjects)

print("\nDiscard Subject")
subjects.discard("Java")
print(subjects)

print("\nMembership")
print("Python" in subjects)

print("\nLoop")

for subject in subjects:
    print(subject)

print("\nSet Operations")

set1 = {"Python", "C", "Java"}

set2 = {"Java", "Flask", "Python"}

print("\nUnion")
print(set1 | set2)

print("\nIntersection")
print(set1 & set2)

print("\nDifference")
print(set1 - set2)

print("\nSymmetric Difference")
print(set1 ^ set2)

print("=" * 50)