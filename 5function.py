# Without return
# def greet(input):
#     if "Hi" or "hi" in input:
#         print("Hi to you too!")
#     else:
#         print("I dont understand.")
# greet("hi there!")

# Return
def greet(input):
    if "hi" or "Hi" in input:
        return "Hi to you too!"
    else:
        "I dont understand."
greeting = greet("hi there!")
print("Hmm.." + greeting)
print(f"Hmm.. {greeting}")