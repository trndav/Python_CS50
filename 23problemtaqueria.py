def main():
    usr_inp()

def usr_inp():
    menu = { "Baja Taco": 4.25, "Burrito": 7.50, "Bowl": 8.50, "Nachos": 11.00, "Quesadilla": 8.50,
     "Super Burrito": 8.50, "Super Quesadilla": 9.50, "Taco": 3.00, "Tortilla Salad": 8.00 }
    lst = []
    while True:
        try:
            user_input = input("Item: ")
            if user_input.title() in menu:
                lst.append(menu[user_input.title()])
                print(f"Total: ${sum(lst):.2f}")
        except EOFError:
            print()   
            break        
main()
