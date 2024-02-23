# https://www.youtube.com/watch?v=lox29cXvwnk&list=PL7yh-TELLS1FuqLSjl5bgiQIEH25VEmIc&index=3

import sys

def generator(x):    
    for x in range(x):
        yield x ** 2 # next element and dont finish function

values = generator(9)

print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))

for x in values:
    print(x)

print(sys.getsizeof(values)) # Value is alvays same size in bytes no matter if x is bigger