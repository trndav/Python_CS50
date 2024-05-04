zeros = [0, 1] * 10
print(zeros)

zeros2 = (0, 1) * 10
print(zeros2)

def func(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])
func(2, 3, 4, 5, 6, seven=7, eight=8)

# unpack list
somelist = [1, 2, 3, 5]
print(somelist)
print(*somelist)


numbers = [1, 2, 3, 4, 5, 6]
*start, end = numbers 
print("Start", start)
print("End", end)


# Merge tuple and list
some_tuple = (1, 2, 3)
some_list = [5, 6, 7]
merged = [*some_tuple, *some_list]
print("Merged tuple and list:", merged)

# Merge dictionaries
dict1 = {'a': 4, 'b': 7}
dict2 = {'c': 8, 'd': 9}
merged_dict = {**dict1, **dict2}
print(merged_dict)