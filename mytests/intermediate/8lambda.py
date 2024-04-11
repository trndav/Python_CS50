# lambda argument: expression

add10 = lambda x: x + 10
print(add10(5))

def add10f(x):
    return x + 10
print(add10f(6))

mult = lambda x,y: x * y 
print(mult(2,5))

mylist = [(1, 2), (15, 1), (5, -1), (10, 4)]
mylist_sorted = sorted(mylist)
print(mylist)
print(mylist_sorted)

mylist = [(1, 2), (15, 1), (5, -1), (10, 4)]
mylist_sorted = sorted(mylist, key=lambda x: x[1]) # Lambda - cheaper than using function like bellow
print(mylist)
print(mylist_sorted)
for i in mylist:
    print(i[1])

mylist = [(1, 2), (15, 1), (5, -1), (10, 4)]
def sort_by_y(x):
    return x[1]
mylist_sorted = sorted(mylist, key=sort_by_y) # 
print(mylist)
print(mylist_sorted)

mylist = [(1, 2), (15, 1), (5, -1), (10, 4)]
mylist_sorted = sorted(mylist, key=lambda x: x[0] + x[1]) # Lambda - sum of tuples
print(mylist)
print(mylist_sorted)

# map(func, seq)
a = [ 1, 2, 3, 4, 5]
b = map(lambda x: x * 2, a)
print(b)
print(list(b))
c = [x * 2 for x in a]
print(c)


import timeit
a = [1, 2, 3, 4, 5]
# Timing for b
setup_b = """
a = [1, 2, 3, 4, 5]
b = map(lambda x: x * 2, a)
"""
time_b = timeit.timeit(stmt="list(b)", setup=setup_b, number=10000)
# Or shorter: time_b = timeit.timeit(stmt="list(map(lambda x: x * 2, [1, 2, 3, 4, 5]))", number=1000000)
# Timing for c
setup_c = """
a = [1, 2, 3, 4, 5]
"""
time_c = timeit.timeit(stmt="[x * 2 for x in a]", setup=setup_c, number=10000)
# Shorter: time_c = timeit.timeit(stmt="[x * 2 for x in [1, 2, 3, 4, 5]]", number=1000000)
print("Time taken for b:", time_b)
print("Time taken for c:", time_c)

# filter(func, seq)
a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 2 == 0, a)
timeb = timeit.timeit(stmt="list(map(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))", number=10000)
print(list(b))
print(f"Timeb is: {timeb}")

c = [x for x in a if x % 2 == 0]
timec = timeit.timeit(stmt="[x for x in [1, 2, 3, 4, 5, 6] if x % 2 == 0]", number=10000)
print(c)
print(f"Timec is: {timec}")

# reduce(func, seq)
from functools import reduce
a = [1, 2, 3, 4]
product_a = reduce(lambda x,y: x * y, a)
print(product_a)
