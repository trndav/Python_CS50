# Adding to iterator
# x = 0
# while x < 3:
#     print("Hi there!")
#     x = x+1

# Substract from iterator
# x = 3
# while x != 0:
#     print("Hi there!")
#     x += 1

# For loop and list
# for i in [1, 2, 3]:
#     print("Hi there!")

# x = [1, 2, 3]
# for i in x:
#     print("Hi there!")

# Range of values
# for i in range(3):
#     print("Hi there!")

# Using _ because we do not need variable name later
# for _ in range(3):
#     print("Hi there!")

# Pythonic
# print("Hi there with no end=\n" * 3, end="")
# # Or
# print("Hi there with end=\n" * 3)

# while True:
#     n = int(input("What is n?"))
#     if n < 0:
#         continue
#     else:
#         break

# while True:
#     n = int(input("What is n? "))
#     if n > 0:
#         print("Hi there with end=\n" * n, end="")       
#         break

# while True:
#     n = int(input("What is n? "))
#     if n > 0:    
#         break
# for _ in range(n):
#     print("Hi there!")

# Main with functions
# def main():
#     number = get_number()
#     speak(number)
# def get_number():
#     while True:
#         n = int(input("What is n? "))
#         if n > 0:
#             return n
# def speak(n):
#     for _ in range(n):
#         print("Hi there!")
# main()

# Other way
def main():
    number = get_number()
    speak(number)
def get_number():
    while True:
        n = int(input("What is n? "))
        if n > 0:
            break 
    return n
def speak(n):
    for _ in range(n):
        print("Hi there!")
main()