# import numpy as np

# a = np.array([0, 1, 2, 3, 4])
# print(a)
# print(type(a))
# print(np.__version__)
# print(a.dtype)

# a[4] = 8
# print(a)

# d = a[1:3]
# print(d)

# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print("Slicing:", arr[1:5:2])

# select = [0, 2, 3, 4]
# e = arr[select]
# print(e)
# print(arr)


# a = np.array([0, 1, 2, 3, 4])
# print(a.size)
# print(a.ndim)
# print(a.shape)

# mean = a.mean()
# print("Mean:",mean)
# standard_deviation=a.std()
# print("Std.dev:", standard_deviation)

# max_a = a.max()
# min_a = a.min()
# print(f"Max a and min_a:", {max_a}, {min_a})


# c = np.array([-10, 201, 43, 94, 502])
# min = c.min()
# max = c.max()
# Sum = (max +min)
# print(Sum)


import time 
import sys
import numpy as np 
import matplotlib.pyplot as plt

u = np.array([1, 0])
v = np.array([0, 1])
z = np.add(u, v)
print(z)

# def Plotvec1(u, z, v):    
#     ax = plt.axes() # to generate the full window axes
#     ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)# Add an arrow to the  U Axes with arrow head width 0.05, color red and arrow head length 0.1
#     plt.text(*(u + 0.1), 'u')#Adds the text u to the Axes 
    
#     ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)# Add an arrow to the  v Axes with arrow head width 0.05, color red and arrow head length 0.1
#     plt.text(*(v + 0.1), 'v')#Adds the text v to the Axes 
    
#     ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
#     plt.text(*(z + 0.1), 'z')#Adds the text z to the Axes 
#     plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
#     plt.xlim(-2, 2)#set the xlim to left(-2), right(2)
# Plotvec1(u, z, v)

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
ab = np.add(arr1, arr2)
print(ab)

ac = np.subtract(arr1, arr2)
print(ac)

x = np.array([3, 2])
y = np.array([2, 4])
ar = np.multiply(x, y)
print(ar)


w = np.array([8, 18, 32])
s = np.array([2, 6, 4])
ws = np.divide(w, s)
print(ws)

arr4 = np.array([3, 5])
arr5 = np.array([2, 4])
arr6 = np.dot(arr4, arr5)
print("Arr6: ", arr6)

ay = np.array([1, 2, 3, -1])
yy = ay + 5
print(yy)


np.pi
xpi = np.array([0, np.pi/2 , np.pi]) # Create the numpy array in radians
ypi = np.sin(xpi)
print(xpi)
print(ypi)


print(np.linspace(-2, 2, num=5))


