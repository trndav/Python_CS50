
# Simple function
# def hello():
#     print(f"Hi {name}")
# name = input("What is your name? ")
# hello()

# Call function with input name
# def hello(to):
#     print("Hi", to, "!")
# name = input("What is your name? ")
# hello(name)

# Triggering hello() without value
# def hello(to="world"):
#     print("Hi", to, "!")
# hello() # Without argument
# name = input("What is your name? ")
# hello(name) # With argument

# Using main() for functions called later, before main()
def main():
    name = input("What is your name? ")
    hello(name)    
def hello(to="world"):
    print("Hi", to, "!")
hello()
main()
