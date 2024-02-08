# SyntaxError - unterminated string literal
# print("Hi there)

# ValueError - Invalid literal if input not int
# user_input = int(input("What is x? "))
# print(f"user_input is {user_input}")

# Try ValueError
# try: 
#     user_input = int(input("What is x? "))
#     print(f"user_input is {user_input}")
# except ValueError:
#     print(f"Input is not integer. Must enter integer.")

#NameError - bc error happens before string/int is assigned to x
# try: 
#     user_input = int(input("What is x? "))
# except ValueError:
#     print(f"Input is not integer. Must enter integer.")    
# print(f"user_input is {user_input}")

# Try except else
# try: 
#     user_input = int(input("What is x? "))
# except ValueError:
#     print(f"Input is not integer. Must enter integer.")   
# else: 
#     print(f"user_input is {user_input}")

# While try except else
# while True:
#     try: 
#         user_input = int(input("What is x? "))
#     except ValueError:
#         print(f"Input is not integer. Must enter integer.")   
#     else: 
#         break
# print(f"user_input is {user_input}")

# While Try Except no Else
# while True:
#     try: 
#         user_input = int(input("What is x? "))
#         break
#     except ValueError:
#         print(f"Input is not integer.")   
# print(f"user_input is {user_input}")

# Function While try Except
# def main():
#     x = get_int()
#     print(f"User input, x is: {x}")
# def get_int():
#     while True:
#         try: 
#             user_input = int(input("What is x? "))
#             break
#         except ValueError:
#             print(f"Input is not integer.")   
#     return user_input
# main()

# Or
# def main():
#     x = get_int()
#     print(f"User input, x is: {x}")
# def get_int():
#     while True:
#         try: 
#             user_input = int(input("What is x? "))            
#         except ValueError:
#             print(f"Input is not integer.")   
#         else:
#             break
#     return user_input
# main()

# Function shorter
# def main():
#     x = get_int()
#     print(f"User input, x is: {x}")
# def get_int():
#     while True:
#         try: 
#             user_input = int(input("What is x? "))            
#         except ValueError:
#             print(f"Input is not integer.")   
#         else:
#             return user_input
# main()

# Function shorter
# def main():
#     x = get_int()
#     print(f"User input, x is: {x}")
# def get_int():
#     while True:
#         try: 
#             user_input = int(input("What is x? "))      
#             return user_input      
#         except ValueError:
#             print(f"Input is not integer.")               
# main()

# Function shorter
# def main():
#     x = get_int()
#     print(f"User input, x is: {x}")
# def get_int():
#     while True:
#         try: 
#             return int(input("What is x? "))     
#         except ValueError:
#             print(f"Input is not integer.") # Or pass
# main()

# Pass exception
# def main():
#     x = get_int()
#     print(f"User input, x is: {x}")
# def get_int():
#     while True:
#         try: 
#             return int(input("What is x? "))     
#         except ValueError:
#             pass
# main()

# More reusable
def main():
    x = get_int("What is x? ")
    print(f"User input, x is: {x}")
def get_int(prompt):
    while True:
        try: 
            return int(input(prompt))     
        except ValueError:
            pass
main()