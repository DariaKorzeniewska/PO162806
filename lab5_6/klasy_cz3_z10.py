# zad10
class Student:
    def __init__(self, student_id=10, student_name="Adam Nowak"):
        self.student_id = student_id
        self.student_name = student_name

student1 = Student()
print(student1.__dict__)
student1.__setattr__("student_class", "1C")
print(student1.__dict__)
student1.__delattr__("student_name")
print(student1.__dict__)







