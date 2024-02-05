user_input = input("Input: ")

user_input.lower()
x = user_input.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "")
print(f"Output: {x}")
