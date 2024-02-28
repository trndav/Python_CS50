
# # First bad/old way
# class Investor:
#     def __init__(self, name: str, age: int, cash: float):
#         self.name = name
#         self.age = age
#         self.cash = cash

#     # def __repr__(self):
#     #     return f"Name is: {self.name}"
#     # Or
#     def __str__(self):
#         return f"Name is: {self.name}, age: {self.age}, cash: {self.cash}."
    
#     def __eq__(self, other):
#         return self.name == other.name
    
#     def __lt__(self, other):
#         return self.cash < other.cash

# i1 = Investor("Bob", 29, 19000)
# i2 = Investor("Tim", 19, 3000)
# i3 = Investor("Gogo", 23, 13000)
# i4 = Investor("Bob", 29, 9000)

# print(i1 == i4)
# print(i1 > i4) # __lt__


# Now we can add new class fields easier
# To remove field from repr we use field
# from dataclasses import dataclass, field

# @dataclass #no need to provide constructor
# class Investor:
#     name: str
#     age: int
#     cash: float
#     sport: str = field(repr=False, compare=False, default="No sport") # sport does not show in repr/str if repr=false

#     # def __repr__(self):
#     #     return f"This 'overwrites' other stuff"

# i1= Investor("Bob", 24, 5000, "Football")
# i2= Investor("Mike", 30, 3000, "Basketball")
# i3= Investor("Bob", 24, 5000)

# print(i3) # We can use it bc of dataclasses
# print(i1 == i3) # Compare is removed for sport

# Custom way of sorting index like cash
from dataclasses import dataclass, field

@dataclass(order=True) #no need to provide constructor
class Investor:
    sort_index: float = field(init=False, repr=False) # Field wont be initialized
    name: str
    age: int
    cash: float
    sport: str = field(repr=False, compare=False, default="No sport") # sport does not show in repr/str if repr=false

    def __post_init__(self):
        self.sort_index = self.cash

i1= Investor("Bob", 24, 5000, "Football")
i2= Investor("Mike", 30, 3000, "Basketball")
i3= Investor("Bob", 24, 6000)

print(i3) # We can use it bc of dataclasses
print(i1 > i2) # Compare is removed for sport

# To sort investory by cash, with list:
lst = [i1, i2, i3]
lst.sort()
print(lst)

