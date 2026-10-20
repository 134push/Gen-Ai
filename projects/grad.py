student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student, score in student_scores.items():
    if score >= 90:
        student_grades[student] = "Excellent"
    elif score >= 80:
        student_grades[student] = "Good"
    elif score >= 60:
        student_grades[student] = "Keep growing"
    elif score >= 40:
        student_grades[student] = "You need improvement"
    else:
        student_grades[student] = "Fail"

print(student_grades)