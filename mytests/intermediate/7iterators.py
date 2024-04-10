# Iterators module: product, permutations, combinations, accumulate, groupby, infinite iterators
from itertools import product 
a = [1, 2]
b = [3, 4]
prod = product(a,b)
print(prod)
print(list(prod))

b = [3]
prod = product(a,b, repeat=2)
print(list(prod))

from itertools import permutations
a = [1, 2, 3]
perm = permutations(a)
print(list(perm))

perm = permutations(a, 2) # Length of permutation
print(list(perm))

print("*" *9)

from itertools import combinations 
a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))

from itertools import combinations, combinations_with_replacement
a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

from itertools import accumulate 
a = [1, 2, 3, 4, 5, 6]
acc = accumulate(a)
print(a)
print(list(acc))

from itertools import accumulate 
import operator
a = [1, 2, 3, 4, 5, 6]
acc = accumulate(a, func=operator.mul)
print(a)
print(list(acc))

print("*" *9)
from itertools import accumulate 
import operator
a = [1, 2, 7, 3, 4, 5, 6]
acc = accumulate(a, func=max)
print(a)
print(list(acc))

from itertools import groupby 
def smaller_than_3(x):
    return x < 3

a = [1, 2, 3, 4, 5]
group_obj = groupby(a, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))

print("*" *9)

from itertools import groupby 
a = [1, 2, 3, 4, 5]
group_obj = groupby(a, key=lambda x: x < 3)
for key, value in group_obj:
    print(key, list(value))

print("*" *9)

from itertools import groupby 
persons = [{'name': 'Bob', 'age': 23}, {'name': 'Tim', 'age': 23}, {'name': 'Alice', 'age': 21}, {'name': 'Sas', 'age': 33}]
group_obj = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))


from itertools import count, cycle, repeat 
for i in count(10):
    print(i)
    if i == 15:
        break

from itertools import count, cycle, repeat 
a = [1, 2, 3]
count = 0
for i in cycle(a):
    print(i, end="")
    count += 1
    if count == 15:
        break

from itertools import repeat 
for i in repeat(1, 3):
    print(i)
