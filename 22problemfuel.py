def main():
    fuel()

def fuel():
    while True:
        try:
            user_input = input("Fraction: ")
            a, b = user_input.split("/")
            a = int(a)
            b = int(b)
            percent = a/b*100.00
            percentage = round(percent)
            if a > b:
                continue
            if percentage >= 99:
                print("F")
                break
            elif percentage <= 1:
                print("E")
                break
            else:
                print(f"{percentage}%")
                break
        except ValueError:
            pass
        except ZeroDivisionError:          
            pass
main()


