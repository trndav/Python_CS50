# Code need fixing Value/Zero errors, and gauge() should get input from convert()

def main():
    user_input = input("Fraction: ")

    if convert(user_input) != 100 and convert(user_input) != 1:
        print(f"{convert(user_input)}%")
    if gauge(user_input) is not None:
        print(f"{gauge(user_input)}")

def convert(inp):
    while True:
        try:
            a, b = inp.split("/")
            a = int(a)
            b = int(b)
            if b == 0:
                raise ZeroDivisionError
            percent = a/b*100.00
            percentage = round(percent)
            if a > b:
                return ValueError
            # if percentage >= 99:
            #     return "F"
            # elif percentage <= 1:
            #     return "E"
            return percentage
        except ValueError:
            raise ValueError
        # except ZeroDivisionError:
        #     raise ZeroDivisionError
def gauge(inp):
    a, b = inp.split("/")
    a = int(a)
    b = int(b)
    if b == 0:
        raise ZeroDivisionError
    percent = a/b*100.00
    percentage = round(percent)
    if a > b:
        return ValueError
    elif percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        pass

if __name__ == "__main__":
    main()


