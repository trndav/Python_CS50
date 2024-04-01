mylist = ["bob", "gog", "apa"]
print(mylist)

for i in mylist:
    print(i)

if "bob" in mylist:
    print("It is there!")
else:
    print("It is not there!")

print(len(mylist))

mylist.append("sasa")
print(mylist)

# Add to list index
mylist.insert(1, "sky")
print(mylist)

# Remove from list (last item), or by index
mylist.pop()
print(mylist)
mylist.pop(2)
print(mylist)

# Remove by name
mylist.remove("apa")
print(mylist)

# Delete all elements in list
#mylist.clear()
#print(mylist)

# Reverse
mylist.append("appo")
mylist.reverse()
print(mylist)

# sort number list
numlist = [1, 5, 7, 3, -8]
numlist.sort()
print(sorted(numlist))
print(numlist)

list2 = [2] * 5
print(list2)

# combine 2 lists
print(numlist + list2)

# Slicing list
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = list3[1:5] # can be like (:5), (5:)
print(a)

# select every second element
b = list3[::2]
print(b)
c = list3[::3]
print(c)

# Copy list
list4 = ["banana", "apple", "pear"]
list_copy = list4 
print(list_copy)
list_copy.append("lemon")
print(list_copy)

# List comprehension, new list from existing
list5 = [1, 2, 3, 4, 5, 6]
a = [i*i for i in list5]
print(list5)
print(a)