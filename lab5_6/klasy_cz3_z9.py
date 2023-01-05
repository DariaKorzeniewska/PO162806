#zad 9
class Student:
    def __init__(self, student_name="Adam", marks=[1, 2, 3]):
        self.student_name = student_name
        self.marks = marks
student1 = Student()
print(student1.__dict__)
student1.__setattr__("student_name", "Martyna")
student1.__setattr__("marks", [4, 5, 6])
print(student1.__dict__)


