# def main():
#     yell("This is CS50")
# def yell(phrase):
#     print(phrase.upper())
# if __name__ == "__main__":
#     main()

# # Unpacked
# def main():
#     yell(["This", "is", "CS50"])

# def yell(words):
#     uppercased = []
#     for word in words:
#         uppercased.append(word.upper())
#     # print(uppercased)
#     print(*uppercased) # unpacked
 
# if __name__ == "__main__":
#     main()

# unpacking
# def main():
#     yell("This", "is", "CS50")

# def yell(*words): # unpacking
#     uppercased = []
#     for word in words:
#         uppercased.append(word.upper())
#     # print(uppercased)
#     print(*uppercased) # unpacked
 
# if __name__ == "__main__":
#     main()

# mapping
# def main():
#     yell("This", "is", "CS50")

# def yell(*words): # unpacking
#     uppercased: str = map(str.upper, words) # upper for every word, no ()
    
#     print(*uppercased) # unpacked
 
# if __name__ == "__main__":
#     main()

# list comprehension
def main():
    yell("This", "is", "CS50")

def yell(*words): # unpacking
    uppercased: list = [word.upper() for ford in words] # list comprehension
    
    print(*uppercased) # unpacked
 
if __name__ == "__main__":
    main()