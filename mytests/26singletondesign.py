# https://www.youtube.com/watch?v=Qb4rMvFRLJw&list=PL7yh-TELLS1FuqLSjl5bgiQIEH25VEmIc&index=9

from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):
    @abstractstaticmethod
    def print_data():
        ''' Implement in child class '''

class PersonSingleton(IPerson):
    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance == None:
            PersonSingleton("Default Name", 0)
        return PersonSingleton.__instance
    
    def __init__(self, name, age):
        if PersonSingleton.__instance != None:
            raise Exception("Singleton cant be instantiated more than once")
        else:
            self.name = name 
            self.age = age 
            PersonSingleton.__instance = self 

    @staticmethod
    def print_data():
        print(f"Name: {PersonSingleton.__instance.name}, Age: {PersonSingleton.__instance.age}")

p = PersonSingleton("Mike", 30)
print(p)
p.print_data()