# *args **kwargs

# def f(*args, **kwargs):  # Takes undefined number of arguments and keyword arguments (convention)
#     print("Positional:", args)
# f(100, 500, 25, 5)

def f(*args, **kwargs):  
    print("Named:", kwargs) # will create dictionary f(key=value,)

f(galleons=100, sickles=50, knuts=25, cents=5)