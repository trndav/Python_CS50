
def print_name(name):
    print(name)

print_name("Bob")

def foo(a, b, c):
    print(a, b, c)

foo(1, 2, 3)
foo(c=1, b=2, a=3)
foo(1, b=2, c=3)

def fo(a, b, c, d=4):
    print(a, b, c, d)

fo(1, 2, 3, 7)

def foo2(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])
foo2(1, 2, 3, 4, 5, six=6, seven=7)


def foo3(a, b, *, c, d):
    print(a, b, c, d)
foo3(1, 2, c=3, d=4)

def foo4(*args, last):
    for arg in args:
        print(arg)
    print(last)
foo4(1, 2, 3, last=100)

def foo5(a, b, c):
    print(a, b, c)
mylist = [0, 1, 2]
foo5(*mylist) #unpack

def foo6(a, b, c):
    print(a, b, c)
mylist = (0, 1, 3)
foo6(*mylist) #unpack

def foo7(a, b, c):
    print("foo7 unpack", a, b, c)
mydict2 = {'a':3, 'b':4, 'c':6}
foo7(**mydict2) #unpack

def foo8():
    x = number
    print('number inside function: ', x)
number = 0
foo8() 

def foo8():
    global number
    x = number
    number = 4
    print('number inside function: ', x)
number = 0
foo8() 
print(number)


def foo9(a_list):
    a_list.append(4)
    a_list[0] = -100
mylist1 = [1, 2, 3]
foo9(mylist1)
print(mylist1)