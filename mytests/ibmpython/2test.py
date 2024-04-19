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