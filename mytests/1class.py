
class Person:
    def __init__(self, age, weight, first_name, password):
        self.age = age
        self.weight = weight
        self.first_name = first_name 
        self.password = password
    
    def walk(self):
        return "walking now.."
    
    def run(self):
        return "running!"

# Instance of Person class
user = Person(25, 80, "Bob", "123456")

print(user.first_name + " is " + user.walk())
user.walk()
print(f"{user.first_name} is {user.run()}")