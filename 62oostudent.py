# @classmethod
class Student:
    def __init__(self, name, house):  # Instance method - initialization of object
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}" # method prints "a student" when print(student) is called

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house) # Instantiate student object

def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()