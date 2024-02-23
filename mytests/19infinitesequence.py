import sys

def infinite_sequence():
    result = 1
    while True:
        yield result
        result *=2

values = infinite_sequence()

print(next(values))
print(next(values))
print(next(values))
print(next(values))

print(sys.getsizeof(values))