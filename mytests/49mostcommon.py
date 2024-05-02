# from collections import Counter
# my_list = [1, 2, 3, 2, 1, 3, 1, 1, 2, 3, 4, 5]
# counter = Counter(my_list)
# most_common_elements = counter.most_common()
# print(most_common_elements)


# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# # Using list comprehensions
# intersection = [item for item in list1 if item in list2]
# print(intersection)
# # Using set operations
# intersection2 = list(set(list1) & set(list2))
# print(intersection2)


# my_list = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}, {"name": "Charlie", "age": 35}]
# sorted_list = sorted(my_list, key=lambda x: x["age"])
# print(sorted_list)


# import time
# def timer_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         execution_time_ms = (end_time - start_time) * 1000
#         print(f"{func.__name__} took {execution_time_ms:.8f} milliseconds to execute")
#         return result
#     return wrapper
# @timer_decorator
# def my_function(n):
#     result = 0
#     for i in range(1, n+1):
#         result += i ** 2 * (i % 3)
#     return result
# my_function(10000)


# def flatten_list(x):
#     result = []
#     for item in x:
#         if isinstance(item, list):
#             result.extend(flatten_list(item))
#         else:
#             result.append(item)
#     return result
# nested_list = [1, [2, [3, 4], 5], 6, [7, 8]]
# flat_list = flatten_list(nested_list)
# print(flat_list)


# def longest_common_prefix(strings):
#     prefix = []
#     for chars in zip(*strings):
#         if len(set(chars)) == 1:
#             prefix.append(chars[0])
#         else:
#             break
#     return "".join(prefix)
# strings = ["flower", "flow", "flight"]
# prefix = longest_common_prefix(strings)
# print(prefix)


# from collections import OrderedDict
# def first_non_repeated_char(x):
#     char_count = OrderedDict()
#     for char in x:
#         char_count[char] = char_count.get(char, 0) + 1

#     for char, count in char_count.items():
#         if count == 1:
#             return char
# string = "otorinolaringologijat"
# result = first_non_repeated_char(string)  # j
# print(result)


# def divide(a, b):
#     try:
#         result = a / b
#     except ZeroDivisionError:
#         print("Error: Division by zero is not allowed.")
#     except TypeError:
#         print("Error: Invalid input types. Both arguments must be numbers.")
#     else:
#         print(f"Result: {result}")
#     finally:
#         print("Division operation completed.")
# divide(10, 2)  # Result: 5.0, Division operation completed.


# nums = set([1, 1, 2, 2, 3, 3, 3, 4])
# print(len(nums))
# a=(1,2,3)
# a[1]=4
# print(a)


x = 1
while x < 5:
    x *= 2
    print(x)