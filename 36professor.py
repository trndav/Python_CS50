import random

def main():
    generate_integer(get_level())

def get_level():
    while True:
        user_input = input("Level: ")
        if user_input.isnumeric():
            user_input = int(user_input)
            if user_input in range(1,4):
                #print(user_input)
                return user_input
            else:
                continue

def generate_integer(level):
    if level == 1:
        counter = 10
        correct = 0
        while counter > 0:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            errcount = 3
            while True:
                answer = int(input(f"{x} + {y} = "))
                if answer == x + y:
                    counter = counter - 1
                    correct = correct + 1
                    break
                else:
                    print("EEE")
                    errcount = errcount - 1
                    counter = counter - 1
                    if errcount == 0:
                        print(f"{x} + {y} = {x + y}")
                        break
        print(f"Score: {correct}")
    elif level == 2:
        counter = 10
        correct = 0
        while counter > 0:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
            errcount = 3
            while True:
                answer = int(input(f"{x} + {y} = "))
                if answer == x + y:
                    counter = counter - 1
                    correct = correct + 1
                    break
                else:
                    print("EEE")
                    errcount = errcount - 1
                    counter = counter - 1
                    if errcount == 0:
                        print(f"{x} + {y} = {x + y}")
                        break
        print(f"Score: {correct}")
    elif level == 3:
        counter = 10
        correct = 0
        while counter > 0:
            x = random.randint(100, 999)
            y = random.randint(100, 999)
            errcount = 3
            while True:
                answer = int(input(f"{x} + {y} = "))
                if answer == x + y:
                    counter = counter - 1
                    correct = correct + 1
                    break
                else:
                    print("EEE")
                    errcount = errcount - 1
                    counter = counter - 1
                    if errcount == 0:
                        print(f"{x} + {y} = {x + y}")
                        break
        print(f"Score: {correct}")

if __name__ == "__main__":
    main()
