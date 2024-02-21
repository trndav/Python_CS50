# https://www.youtube.com/watch?v=39m3rstTN8w&list=PLzMcBGfZo4-l1MqB1zoYfqzlj_HH-ZzXt&index=4

# Wthout __str__
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
print(p1)

# With __str__
class Person2:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person2("John", 36)
print(p1)

class Person3:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name + " and I am " + str(self.age) + " years old.")

p1 = Person3("John", 36)
p1.myfunc()