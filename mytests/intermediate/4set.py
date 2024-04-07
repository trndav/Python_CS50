# Set undordered, mutable, no duplicates

myset = {1, 2, 3}
print(myset)
set2 = {1, 2, 3, 1, 2}
print(set2)

set3 = set([1, 2, 3, 4])
print(set3)

set4 = set("Hola")
print(set4) # Unordered

# Empty set
set5 = set()
print(type(set5))

myset.add(10)
myset.add(15)
print(myset)
myset.remove(1)
print(myset)
myset.discard(2)
print(myset)

for i in set2:
    print(i)

if 2 in set3:
    print("Yes")

# union, intersection

seta = {1, 3, 5, 7, 9}
setb = {0, 2, 4, 6, 8, 9}
primes = {2, 3, 5, 7}

u = seta.union(setb) # combine sets
print(u)
i = seta.intersection(setb) # Copy only elements that are in both sets
print(i)

print("*"*9)

setd = {1, 2, 3, 4, 5, 6, 7, 8, 9}
sete = {1, 2, 3, 10, 11, 12}
diff = setd.difference(sete) # Copy elements from first set that are not in set2
print(diff)

setf = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setg = {1, 2, 3, 10, 11, 12}
diff2 = setf.symmetric_difference(setg) # Copy unique elements from both sets that dont repeat
print(diff2)
setf.update(setg) # Copy all unique elements from b to a
print(setf)

print("*"*9)

set11 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set22 = {1, 2, 3, 10, 11, 12}
set11.intersection_update(set22) # Copy elements that repeats in A and B
print(set11)

set11 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set22 = {1, 2, 3, 10, 11, 12}
set11.difference_update(set22) # Copy elements that do not repeat to a, from b
print(set11)

set11 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set22 = {1, 2, 3, 10, 11, 12}
set11.symmetric_difference(set22) # 
print(set11)

set33 = {1, 2, 3, 4, 5, 6}
set44 = {1, 2, 3}
print(set33.issubset(set44)) # False
print(set44.issubset(set33)) # True

print(set33.issuperset(set44)) # True
print(set44.issuperset(set33)) # False

set55 = {7, 8}
print(set33.isdisjoint(set44)) # False
print(set33.isdisjoint(set55)) # True

print("*"*9)

set33 = {1, 2, 3, 4, 5, 6}
set44 = set33
set44.add(7)
print(set44)
print(set33)

set33 = {1, 2, 3, 4, 5, 6}
set44 = set33.copy()
set44.add(7)
print(set44)
print(set33)

# Copy different way

set33 = {1, 2, 3, 4, 5, 6}
set44 = set(set33)
set44.add(7)
print(set44)
print(set33)

# Frozen set - imutable version

a = frozenset([1, 2, 3, 4, 5])
print(a)
# a.add(5) # Error
print(a)