import time

# Topic 2: Data Types in Python
# Python has several built-in data types:
# 1. Numeric: int, float, complex
# 2. Text: str
# 3. Boolean: bool (True / False)
# 4. Sequence: list, tuple, range
# 5. Mapping: dict
# 6. Set Types: set, frozenset

college_name = "madhuben and bhanubhai college of b.tech"  # str
student_name = "pushpam"                                   # str
student_age = 20                                           # int

current_study_year = "3rd year"                             # str
current_semester = "Semester 5"                             # str
student_branch = "computer engineering"                    # str

previous_semester_cgpa = 8.5                                # float
current_semester_cgpa = 9.0                                 # float

fees_paid = True                                           # bool
fees_amount = 100000                                       # int
fees_payment_date = "2024-01-15"                           # str
fees_payment_method = "online"                             # str

travelling_distance_to_college = 15.5                      # float
travelling_time_to_college = 30                            # int
travelling_mode = "bus"                                    # str

today_attendance_percentage = 95.0                         # float
nata_list = False                                          # bool

projects_completed = 5                                     # int
pending_projects = 2                                       # int
exam_given = True                                          # bool

# Print Student Profile
print("=============================")
time.sleep(0.2)
print("      STUDENT PROFILE")
print("=============================")
print(f"Name: {student_name} ({type(student_name).__name__})")
print(f"Age: {student_age} ({type(student_age).__name__})")
print(f"College: {college_name} ({type(college_name).__name__})")
print(f"Branch: {student_branch} ({type(student_branch).__name__})")
print(f"CGPA: {current_semester_cgpa} ({type(current_semester_cgpa).__name__})")
print(f"Fees Paid: {fees_paid} ({type(fees_paid).__name__})")
print(f"Fees Amount: {fees_amount} ({type(fees_amount).__name__})")
print(f"Travelling Distance: {travelling_distance_to_college} km ({type(travelling_distance_to_college).__name__})")
print(f"Today's Attendance: {today_attendance_percentage}% ({type(today_attendance_percentage).__name__})")
print(f"Projects Completed: {projects_completed} ({type(projects_completed).__name__})")
print(f"Exam Given: {exam_given} ({type(exam_given).__name__})")
print("=============================")

