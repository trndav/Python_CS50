def main():
    greet = input("You are banker, and customer approach and say 'Hello'. What you say? \n")
    print(f"${value(greet)}")

def value(greeting):
    lst = greeting.lower().split()
    if lst[0] == "hello" or lst[0] == "hello,":
        return 0
    elif lst[0][0] == "h":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
