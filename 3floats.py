# Simple float sum
# x = float(input("enter number for x: "))
# y = float(input("enter number for y: "))
# print(x + y)

# Rounded
# x = float(input("enter number for x: "))
# y = float(input("enter number for y: "))
# z = round(x + y, 3) # Round and to 3 decimals
# print(z)

# Rounded and 1,000.00
# x = float(input("enter number for x: "))
# y = float(input("enter number for y: "))
# z = round(x + y, 3) # Round and to 3 decimals
# print(f"{z:,}") # Formats numbr as 1,000.00

# Reounded 2 decimals
# x = float(input("enter number for x: "))
# y = float(input("enter number for y: "))
# z = round(x / y, 2)
# print(z) 

# Rounded 2 decimals formated string :.3f
# x = float(input("enter number for x: "))
# y = float(input("enter number for y: "))
# z = x / y
# print(f"{z:.3f}") 

# Using main() and built square() function
def main():
    x = float(input("enter number for x: "))
    print("Square of x is: ", square(x)) 
def square(n):
    return n * n 
main()