# https://www.youtube.com/watch?v=cMmuAbnG7UU&list=PL7yh-TELLS1FuqLSjl5bgiQIEH25VEmIc&index=8

from abc import ABCMeta, abstractstaticmethod

# class IPerson(metaclass=ABCMeta):
#     @abstractstaticmethod
#     def person_method():

class Person():
    def person_method(self):
        print("I am person")

class ProxyPerson():
    def __init__(self):
        self.person = Person()

    def person_method(self):
        print("I am the proxy functionality")
        self.person.person_method

p1 = Person()
p1.person_method()

p2 = ProxyPerson()
p2.person_method()


# https://www.youtube.com/watch?v=cMmuAbnG7UU&list=PL7yh-TELLS1FuqLSjl5bgiQIEH25VEmIc&index=8

# from abc import ABCMeta, abstractstaticmethod

# class IPerson(metaclass=ABCMeta):
#     @abstractstaticmethod
#     def person_method():
#         '''Interface method'''

# class Person(IPerson):
#     def person_method(self):
#         print("I am person")

# class ProxyPerson(IPerson):
#     def __init__(self):
#         self.person = Person()

#     def person_method(self):
#         print("I am the proxy functionality")
#         self.person.person_method

# p1 = Person()
# p1.person_method()

# p2 = ProxyPerson()
# p2.person_method()