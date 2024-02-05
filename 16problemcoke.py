# def main():
#     print("Amount Due: 50")
#     user_input = int(input("Insert coin: "))
#     calculate(user_input)

# def calculate(user_input):
#     a = 5
#     b = 10
#     c = 25
#     x = 50

#     if user_input in [a, b, c]:
#         match user_input:
#             case five if user_input == a:
#                 print(f"Amount due: {x - a}")
#                 x = x - a
#             case ten if user_input == b:
#                 print(f"Amount due: {x - b}")
#                 x = x - b
#             case twentyfive if user_input == c:
#                 print(f"Amount due: {x - c}")
#                 x = x - c
#     else:
#         print(f"Amount due: {x}")
# main()

# def main():
#     print("Amount Due: 50")
#     x = user_input()
#     calculate(x)

# def user_input():
#     return int(input("Insert coin: "))    

# def calculate(n):
#     a = 5
#     b = 10
#     c = 25
#     if n in [a, b, c]:
#         x = 50
#         if n == a:
#             print(f"Amount due: {x - a}")
#             x = x - a
#             print(f"ax is: {x}")
#             user_input()
#         elif n == b:
#             print(f"Amount due: {x - b}")
#             x = x - b
#             print(f"bx is: {x}")
#             user_input()
#         elif n == c:
#             print(f"Amount c due: {x - c}")
#             x = x - c
#             print(f"cx is: {x}")
#             user_input()
# main()

def main():
    amount_due = 50
    print(f"Amount Due: {amount_due}")
    while amount_due > 0:
        coin = user_input()
        amount_due -= coin
        if amount_due <= 0:
            print(f"Change Owed: {abs(amount_due)}")
        else:
            print(f"Amount Due: {amount_due}")

def user_input():
    amount_due = 50
    coin = int(input("Insert Coin: "))
    while coin not in [5, 10, 25]:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))
    return coin
main()


