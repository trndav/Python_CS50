# Tuples, ordered, immutable, allows duplicate

mytuple = ("Max", 28, "Boston")
print(mytuple)
tuple2 = "Max", 28, "Boston"
print(tuple2)

# 1 element tupple (must be ,)
tuple3 = ("Max",)
print(tuple3)

# Tupple list
tuple4 = tuple(["Max", 28, "Boston"])
print(tuple4)
item = tuple4[2]
print(item)

# From back
item2 = tuple4[-1]
print(item2)

for i in mytuple:
    print(i, ", ", end="")

print()
if "Max" in mytuple:
    print("Yes it is there!")
else:
    print("No!")

tuple5 = ('a', 'd', 'g', 'r', 'c', 'a')
print(len(tuple5))
print(tuple5.count('a'))
print(tuple5.index('d'))

mylist = list(mytuple)
print(mylist)
tuple6 = tuple(mylist)
print(tuple6)

# Slicing tuples

tuple7 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
a = tuple7[2:5]
b = tuple7[:5]
print(a)
print(b)

c = tuple7[1::2] # Every second element starting from index 1
print(c)

d = tuple7[::-1] # Reverse
print(d)

# Unpack
name, age, city = mytuple
print(name, age, city)
print(age, city)
print(city, name)

# Unpack multiple elements
tuple8 = (1, 2, 3, 4, 5, 6, 7)
a, *b, c = tuple8
print(a)
print(b)
print(c)

import sys
mylist = [0, 1, 2, "hi", True]
mytuple = (0, 1, 2, "hi", True)
print(sys.getsizeof(mylist), "bytes")
print(sys.getsizeof(mytuple), "bytes!") # Less bytes

import timeit
print(timeit.timeit(stmt="['lol', 0, 1, 2, 3, 4, 5, 'bombadil']", number=10000000)) # Write 5000 times and count time
print(timeit.timeit(stmt="('lol', 0, 1, 2, 3, 4, 5, 'bombadil')", number=10000000))