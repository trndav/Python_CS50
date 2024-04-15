import random

a = random.random()
print(a) # Float 0-1

a = random.uniform(1, 10)
print(a) # 1 - 10 float

a = random.randint(1, 10)
print(a) # 1 - 10 int

a = random.randrange(1, 10)
print(a) # 1 - 9 - 10 not included

a = random.normalvariate(0, 1) # ?
print(a) 

mylist = list("ABCDEFGH")
a = random.choice(mylist)
print(a)

mylist = list("ABCDEFGH")
a = random.sample(mylist, 2) # Pick random elements, unique
print(a)

mylist = list("ABCDEFGH")
a = random.choices(mylist, k=3) # Pick random elements, not unique, can repeat
print(a)

mylist = list("ABCDEFGH")
random.shuffle(mylist) #
print(mylist)

# Random seed
random.seed(1)
print(random.random())
print(random.randint(1, 10))
print("Repeat will give same numbers")
random.seed(2)
print(random.random())
print(random.randint(1, 10))

print("Secrets")
import secrets
a = secrets.randbelow(10)
print(a) # 0 - 9

a = secrets.randbits(4) # Rand up to 4 bits
print(a) # 0 - 9

mylist = list("ABCDEFGH")
a = secrets.choice(mylist)
print(a)

# Arrays (?) with numpy
import numpy as np
a = np.random.rand(3)
print(a)

a = np.random.randint(0, 10, (3,4)) # 0-10 size + more dimensions
print(a)

arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr)
np.random.shuffle(arr[0])
print(arr)

np.random.seed(1)
print(np.random.rand(3,3))
np.random.seed(1)
print(np.random.rand(3,3))