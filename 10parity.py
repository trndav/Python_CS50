# x = int(input("What is x? "))
# if x % 2 == 0:
#     print("Number is even.")
# else:
#     print("Number is odd.")

# Function is_even()
# def main():
#     x = int(input("What is x? "))
#     if is_even(x):
#         print(" It is even")
#     else:
#         print("It is odd.")
# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
# main()

# Shorter is_even() function
# def main():
#     x = int(input("What is x? "))
#     if is_even(x):
#         print(" It is even")
#     else:
#         print("It is odd.")
# def is_even(n):
#     return True if n % 2 == 0 else False
# main()

# Shortest is_even() function
def main():
    x = int(input("What is x? "))
    if is_even(x):
        print(" It is even")
    else:
        print("It is odd.")
def is_even(n):
    return n % 2 == 0 # Can be only True or False
main()