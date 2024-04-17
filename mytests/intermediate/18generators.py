
# def mygenerator():
#     yield 4
#     yield 2
#     yield 3

# g = mygenerator()
# print(sorted(g))
# print(sum(g))

# print(f"Object: {g}")
# for i in g:
#     print(i)

# value = next(g)
# print(value)

# ******
# def countdown(num):
#     print("Starting")
#     while num > 0:
#         yield num 
#         num -= 1

# cd = countdown(4)
# value = next(cd)
# print(value)
# print(next(cd))
# print(next(cd))
# print(next(cd))
# print(next(cd))



# IMPORTANT
# import sys 
# def firstn(n): # EXPENSIVE MEMORY
#     nums = []
#     num = 0
#     while num < n:
#         nums.append(num)
#         num += 1
#     return nums

# def first_generator(n):  # CHEAP MEMORY
#     num = 0
#     while num < n:
#         yield num
#         num += 1

# print(sys.getsizeof(firstn(10000))) # EXPENSIVE
# print(sys.getsizeof(first_generator(10000))) # CHEAP
# print(sum(first_generator(10)))



# def fibonacci(limit):
#     # 0, 1, 1, 2, 3, 5, 8, 13
#     a, b = 0, 1
#     while a < limit:
#         yield a 
#         a, b = b, a + b 
# fib = fibonacci(30)
# for i in fib:
#     print(i)

import sys
mygenerator = (i for i in range(10000) if i % 2 == 0)
print(mygenerator)
print(sys.getsizeof(mygenerator))

# mygenerator = (i for i in range(10) if i % 2 == 0)
# for i in mygenerator:
#     print(i)

mylist = [i for i in range(10000) if i % 2 == 0]
print(sys.getsizeof(mylist))