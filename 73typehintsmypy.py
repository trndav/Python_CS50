# mypy type hints
# mypy 73typehintsmypy.py

# def meow(n: int):
#     for _ in range(n):
#         print("meow")
# #number: int = int(input("Number: "))
# number: int = input("Number: ")
# meow(number)

# meow do not have return value to print(meows)
# def meow(n: int) -> None:
#     for _ in range(n):
#         print("meow")

# number: int = int(input("Number: "))
# # number: int = input("Number: ")
# meows: str = meow(number)
# print(meows)

def meow(n: int) -> str:
    return "meow\n" * n

number: int = int(input("Number: "))
# number: int = input("Number: ")
meows: str = meow(number)
print(meows, end="")