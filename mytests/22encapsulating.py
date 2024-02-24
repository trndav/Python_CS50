# https://www.youtube.com/watch?v=dzmYoSzL8ok&list=PL7yh-TELLS1FuqLSjl5bgiQIEH25VEmIc&index=5

class Person:
    def __init__(self, name, age, gender):
        self.__name = name # Private vars
        self.__age = age # Private vars
        self.__gender = gender # Private vars

    def __str__(self):
        return str(self.__name) + " " + str(self.__age) + " " + str(self.__gender)
    
    @property
    def Name(self):
        return self.__name
    
    @Name.setter
    def Name(self, value):
        if value == "Bob":
            self.__name = "Default name"
        else:
            self.__name = value
    
    @staticmethod
    def my_method():
        print("Hola!")

Person.my_method()

p1 = Person("Tim", 23, "Male")
print(p1.Name)
p1.Name = "Bob"
print(p1.Name)

Person.my_method()