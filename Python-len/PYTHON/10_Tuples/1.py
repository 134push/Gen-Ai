print("=" * 50)
print("      TUPLE PRACTICE SYSTEM")
print("=" * 50)

subjects = (
    "Python",
    "C",
    "Flask",
    "SQLite",
    "Git"
)

print("\nOriginal Tuple")
print(subjects)

print("\nLength")
print(len(subjects))

print("\nFirst Subject")
print(subjects[0])

print("\nLast Subject")
print(subjects[-1])

print("\nSlicing")
print(subjects[:3])

print("\nReverse")
print(subjects[::-1])

print("\nCount")
print(subjects.count("Python"))

print("\nIndex")
print(subjects.index("SQLite"))

print("\nMembership")
print("Git" in subjects)

print("\nLoop")

for subject in subjects:
    print(subject)

print("\nTuple Unpacking")

a, b, c, d, e = subjects

print(a)
print(b)
print(c)
print(d)
print(e)

print("=" * 50)