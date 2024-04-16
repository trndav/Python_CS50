# Class and function decorators



# @mydecorator # Funct that takes another func as argument
# def dosomething(): # Func is first class object
#     pass

# def start_end_decorator(func):
#     def wrapper():
#         print("Start: ")
#         func()
#         print("End.")
#     return wrapper

# def print_name():
#     print('Alex')

# print_name()
# print_name_var = start_end_decorator(print_name)
# print_name_var()

# # Like above but shorter:
# def start_end_decorator(func):
#     def wrapper():
#         print("Start: ")
#         func()
#         print("End.")
#     return wrapper

# @start_end_decorator
# def print_name():
#     print('Alex')
# print_name()


# To pass arguments from func to decorator, wrapper and func needs *args, **kwargs
# def start_end_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Start:")
#         # print(func(*args, **kwargs))
#         result =  func(*args, **kwargs)
#         print("End.")
#         return result
#     return wrapper

# @start_end_decorator
# def add5(x):
#     return x + 5

# print(add5(3))
# print(help(add5))
# print(add5.__name__)

# import functools
# def start_end_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print("Start:")
#         # print(func(*args, **kwargs))
#         result =  func(*args, **kwargs)
#         print("End.")
#         return result
#     return wrapper

# @start_end_decorator
# def add5(x):
#     return x + 5

# print(add5(3))
# print(help(add5))
# print(add5.__name__)


# import functools

# def repeat(num_times):
#     def decorator_repeat(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             print("Start")
#             for _ in range(num_times):
#                 result = func(*args, **kwargs)            
#             print("End")
#             return result 
#         return wrapper 
#     return decorator_repeat

# @repeat(num_times=5)
# def greet(name):
#     print(f"Hi {name}!")

# greet("Bob")


# Nested decorators
# import functools
# def start_end_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print('Start')
#         result = func(*args, **kwargs)
#         print('End')
#         return result
#     return wrapper

# def debug(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         args_repr = [repr(a) for a in args]
#         kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
#         signature = ", ".join(args_repr + kwargs_repr)
#         print(f"Calling {func.__name__}({signature})")
#         result = func(*args, **kwargs)
#         print(f"{func.__name__!r} returned {result!r}")
#         return result 
#     return wrapper

# @debug
# @start_end_decorator
# def say_hello(name):
#     greeting = f"Hi {name}"
#     print(greeting)
#     return greeting

# say_hello('Bob')



# Class decorators
# Usefull to have time decorator for function (or calls like in example)

class CountCalls:
    def __init__(self, func):
        self.func = func 
        self.num_calls = 0
    
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Number of calls: {self.num_calls}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hi():
    print("Hi")

say_hi()
say_hi()