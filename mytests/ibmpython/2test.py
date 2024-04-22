# fruits = ["apple", "banana", "orange"] 
# more_fruits = ["mango", "grape"] 
# fruits.extend(more_fruits) 
# print(fruits)

# my_list = [1, 2, 3, 4, 5] 
# my_list.insert(6, 7) 
# print(my_list)

# my_list2 = [10, 20, 30, 40, 50] 
# removed_element = my_list2.pop() # Removes and returns the last element 
# print(removed_element) 
# print(my_list2) 

# x = set({"a", "b"} & {"a"})
# print(x)

# for i,fruit in enumerate(fruits):
#     print(i, fruit)


# for i in range(0, 10):
#     multiplied = i * 6
#     print(f"{i} x 6 = {multiplied}")

# for i in range(0, 10):
#     multiplied = i * 7
#     print(f"{i} x 7 = {multiplied}")

# for i in range (10):
#     print("6*",i,"=",6*i)
    
# Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
# for i in Animals:
#     if len(i) == 7:
#         print(i)

# def printDictionary(**args):
#     for key in args:
#         print(key + " : " + args[key])

# printDictionary(Country='Canada',Province='Ontario',City='Toronto')




# x = 0 
# while x < 2: 
#     print(x) 
#     x = x + 1






# class Points(object):
#     def __init__(self, x, y):
#         self.x = x 
#         self.y = y 

#     def print_point(self): 
#         print('x=', self.x, ' y=', self.y) 

# p1 = Points("A", "B") 
# p1.print_point()






# for i, x in enumerate(['A', 'B', 'C']): 
#     print(i, 2 * x)




# class Points(object): 
#     def __init__(self, x, y): 
#         self.x = x 
#         self.y = y 
#     def print_point(self): 
#         print('x=', self.x, ' y=', self.y) 

# p2 = Points(1, 2) 
# p2.x = 'A' 
# p2.print_point()





def sub(a, b):
    return(a + b)
print(sub(1,2))