
lst = [ "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December" ]
while True:
    user_input = input("Date: ")
    if "/" in user_input:
        a, b, c = user_input.split("/")
        a = a.strip()
        b = b.strip()
        c = c.strip()
        if a.isnumeric() and 0 < int(a) <= 12 and b.isnumeric() and 0 < int(b) <= 31 and c.isnumeric():
            print(f"{c}-{int(a):02}-{int(b):02}")
            break
        else:
            continue

    elif " " in user_input:
        a, b, c = user_input.split(" ")
        if "," not in b:
            continue
        else:
            a = a.replace(",", "")
            b = b.replace(",", "")
            c = c.replace(",", "")
            if a in lst and 0 < int(b) < 31:
                    print(f"{c}-{lst.index(a)+1:02}-{int(b):02}")
                    break

