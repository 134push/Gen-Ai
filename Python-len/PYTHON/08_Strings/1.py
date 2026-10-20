print("=" * 50)
print("        STUDENT STRING SYSTEM")
print("=" * 50)

name = input("Enter Full Name : ")
email = input("Enter Email : ")
city = input("Enter City : ")
sentence = input("Enter Your Favourite Sentence : ")

print("\n" + "=" * 50)
print("ORIGINAL DETAILS")
print("=" * 50)

print(f"Name     : {name}")
print(f"Email    : {email}")
print(f"City     : {city}")
print(f"Sentence : {sentence}")

print("\n" + "=" * 50)
print("STRING OPERATIONS")
print("=" * 50)

# Upper
print(f"UPPERCASE : {name.upper()}")

# Lower
print(f"LOWERCASE : {name.lower()}")

# Title
print(f"TITLE CASE : {name.title()}")

# Capitalize
print(f"CAPITALIZE : {name.capitalize()}")

# Strip
print(f"WITHOUT EXTRA SPACE : '{name.strip()}'")

# Replace
print(f"REPLACE : {sentence.replace('Python','Flask')}")

# Find
print(f"Position of 'a' : {name.find('a')}")

# Count
print(f"Total 'a' : {name.count('a')}")

# Startswith
print(f"Starts with 'P' : {name.startswith('P')}")

# Endswith
print(f"Ends with 'a' : {name.endswith('a')}")

# Length
print(f"Length : {len(name)}")

print("\n" + "=" * 50)
print("INDEXING")
print("=" * 50)

print(f"First Character : {name[0]}")
print(f"Last Character : {name[-1]}")

print("\n" + "=" * 50)
print("SLICING")
print("=" * 50)

print(f"First 3 Letters : {name[:3]}")
print(f"Last 3 Letters : {name[-3:]}")
print(f"Reverse : {name[::-1]}")

print("\n" + "=" * 50)
print("SPLIT & JOIN")
print("=" * 50)

words = sentence.split()

print(words)

joined = "-".join(words)

print(joined)

print("\n" + "=" * 50)
print("MEMBERSHIP")
print("=" * 50)

print(f"'Python' in Sentence : {'Python' in sentence}")
print(f"'Java' not in Sentence : {'Java' not in sentence}")

print("\n" + "=" * 50)
print("STRING MULTIPLICATION")
print("=" * 50)

print("⭐" * 20)

print("\nProgram Finished Successfully")