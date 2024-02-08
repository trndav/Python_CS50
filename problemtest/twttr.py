def main():
    user_input = input("Input: ")
    shorten(user_input)
    print(f"Output: {shorten(user_input)}")

def shorten(word):
    x = word.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "").replace("A", "").replace("E", "").replace("I", "").replace("O", "")#.replace("U", "")
    if x.isalpha():
        return x

if __name__ == "__main__":
    main()
