subject = "daa"
total_class = 50

print(f"Total class is {total_class} and subject is {subject}")

class AttendancePercentage:
    def __init__(self, attended_class, total_class):
        self.total_class = total_class
        self.attended_class = attended_class

    def percentage(self):
        return (self.attended_class / self.total_class) * 100

    def percentage_info(self):
        if self.percentage() >= 75:
            return "Eligible for exam ✅"
        else:
            return "Not eligible for exam ❌"

class Student(AttendancePercentage):
    def __init__(self, student_roll_no, name, attended_class, total_class):
        # Parent Class ને બોલાવ્યો:
        super().__init__(attended_class, total_class)
        self.student_roll_no = student_roll_no
        self.name = name

    def student_data(self):
        print(f"Roll No: {self.student_roll_no} || Name: {self.name}")

    def performance(self):
        print(f"Roll No: {self.student_roll_no} || Performance: {self.percentage():.1f}% -> {self.percentage_info()}")



students_db = {}

for i in range(3):
    name = input(f"\nEnter name for student {i+1}: ")
    attended = int(input(f"Enter attended classes for {name}: "))
    roll_no = i + 1

    std_obj = Student(roll_no, name, attended, total_class)
    
    students_db[roll_no] = std_obj

while True:
    print("\n--- MENU ---")
    print("1. Show Student Names")
    print("2. Show Performance & Eligibility")
    print("3. Exit")
    
    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            for roll, std1 in students_db.items():
                std1.student_data()  

        case 2:
            for roll, std1 in students_db.items():
                std1.performance()   

        case 3:
            print("Exiting...")
            break

        case _:
            print("Invalid choice, try again!")