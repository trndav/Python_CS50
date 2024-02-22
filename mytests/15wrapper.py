# Without @mydecorator
# def mydecorator(function):
#     def wrapper():
#         print(" I am decorating function.")
#         function()
#     return wrapper

# def hi_world():
#     print("Hi there!")

# mydecorator(hi_world)()

# With @mydecorator
# def mydecorator(function):
#     def wrapper():
#         print(" I am decorating function.")
#         function()
#     return wrapper

# @mydecorator
# def hi_world():
#     print("Hi there!")

# hi_world()

# Passing argument to wrapper function / cant use return in function
# def mydecorator(function):
#     def wrapper(*args, **kwargs):
#         print(" I am decorating function.")
#         function(*args, **kwargs)
#     return wrapper

# @mydecorator
# def hi(name):
#     print(f"Hi {name}!")

# hi("Bob")

# With return instead of print
# def mydecorator(function):
#     def wrapper(*args, **kwargs):
#         print(" I am decorating function.")
#         return function(*args, **kwargs)    
#     return wrapper

# @mydecorator
# def hi(name):
#     return f"Hi {name}!"

# print(hi("Bob"))

# First execute function then print
def mydecorator(function):
    def wrapper(*args, **kwargs):
        print(" I am decorating function.")  
        return_value = function(*args, **kwargs)          
        return return_value        
    return wrapper

@mydecorator
def hi(name):
    print(f"Hi {name}!")
    return f"Hi {name}!"

print(hi("Bob"))