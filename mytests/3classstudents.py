
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade 

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)

student = Student("Bob", 19, 5)
student2 = Student("Tim", 24, 4)
student3 = Student("Rok", 21, 3)
student.name

course = Course("Woodchopper", 2)
course.add_student(student)
print(course.add_student(student2))
print(course.add_student(student3))
print(course.get_average_grade())