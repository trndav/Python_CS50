# pip install emoji
import emoji
user_input = input("Input: ")
x = emoji.emojize(user_input)
print(emoji.emojize(f"Output: {x}", language='alias'))
