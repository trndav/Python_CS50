fruits = ["apple", "banana", "orange"] 
more_fruits = ["mango", "grape"] 
fruits.extend(more_fruits) 
print(fruits)

my_list = [1, 2, 3, 4, 5] 
my_list.insert(6, 7) 
print(my_list)

my_list2 = [10, 20, 30, 40, 50] 
removed_element = my_list2.pop() # Removes and returns the last element 
print(removed_element) 
print(my_list2) 

x = set({"a", "b"} & {"a"})
print(x)

for i,fruit in enumerate(fruits):
    print(i, fruit)


for i in range(0, 10):
    multiplied = i * 6
    print(f"{i} x 6 = {multiplied}")

for i in range(0, 10):
    multiplied = i * 7
    print(f"{i} x 7 = {multiplied}")

for i in range (10):
    print("6*",i,"=",6*i)
    
Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
for i in Animals:
    if len(i) == 7:
        print(i)

def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])

printDictionary(Country='Canada',Province='Ontario',City='Toronto')