# https://www.youtube.com/watch?v=pqfVGeCX5v4&list=PL7yh-TELLS1F3KytMVZRFO-xIo_S2_Jg1&index=2

class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    
    def __str__(self):
        return f"Person is: {self.name}, {self.age} years old, and {self.height} tall"
    
    def get_older(year):
        self.age += year

class Worker(Person):
    def __init__(self, name, age, height, salary):
        super(Worker, self).__init__(name, age, height)
        self.salary = salary

    def calc_salary(self):
        return self.salary * 12

    def __str__(self):
        text = super(Worker, self).__str__()
        text += f", salary {self.salary}" 
        return text

p1 = Person("Bob", 25, 180)
print(p1)
w1 = Worker("Tim", 23, 176, 10000)
print(w1)
print(w1.calc_salary())