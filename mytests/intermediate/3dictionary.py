# https://www.youtube.com/watch?v=HGOBQPFzWKo&t=1784s
# Mutable

mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

# Dict function
dict2 = dict(name="Harry", age=23, city="Boston")
print(dict2)

value = mydict["name"]
print(value)

# Add new key to dict
mydict["email"] = "some@email.com"
print(mydict)

# Delete
del mydict["name"]
print(mydict)

mydict.pop("age")
print(mydict)
mydict.popitem() # removes last element
print(mydict)

# Check if in dict
if "name" in dict2:
    print(dict2["name"])

try:
    print(dict2["lastname"])
except:
    print("Error")
print("*********")

# Loop
for key in dict2:
    print(key)
for key in dict2.keys():
    print(key)
for value in dict2.values():
    print(value)
for key, value in dict2.items():
    print(key, value)
print("*********")

# copy dictionary
dict_copy = dict2 # Careful! Not really copied, just pointed
print(dict_copy)
dict_copy["admin"] = "No"
print(dict_copy)
print(dict2)

# Real copy:
dict_copy2 = dict2.copy()
dict_copy2["admin"] = "Yes"
print(dict_copy2)
print(dict2)

# OR copy:
dict_copy3 = dict(dict2)
dict_copy3["bro"] = "Yes"
print(dict_copy3)
print(dict2)

print("*********")

# Merge dicts
dict3 = {"name": "Bob", "age": 22, "city": "London"}
dict4 = dict(name="admin", age=33, email="bro@email.com")
dict3.update(dict4)
print(dict3)

dict5 = {3: 9, 6: 36, 9: 81}
print(dict5)

# Using tuple
mytuple = (8, 7)
dict6 = {mytuple: 15}
print(dict6)