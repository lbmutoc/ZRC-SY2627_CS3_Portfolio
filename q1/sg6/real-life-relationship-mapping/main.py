# Write a short Python code snippet showing a Course adding a Student object to a class Student:
    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self, name):
        self.name = name
        self.student = []

    def add_student(self, student):
        self.student.append(student)
