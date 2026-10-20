# 4. Hotel Room Booking System

age = int(input("Enter your age: "))

if age >= 18:
    is_available = input("Is a room available? (yes/no): ").strip().lower()
    if is_available == "yes":
        print("Room Booked Successfully!")
    else:
        print("Booking Rejected: Room Not Available")
else:
    print("Booking Rejected: Must be 18 or older")
