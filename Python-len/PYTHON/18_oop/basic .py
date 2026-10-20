# basic method

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Pushpam", 20)  


print(student1.name)
print(student1.age)

# instance attributes 

class Student:

    college = "mbit"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name)
        print(self.marks)
        print(self.college) # class attributes

student1 = Student("Pushpam", 80)  
student1.display()

# class method 

class Student:

    college = "MBIT"

    @classmethod
    def show_college(cls):
        print(cls.college)

Student.show_college()        