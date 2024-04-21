def generic(a):
    try:
        result = a / (a - 5)
        print(result)
    except Exception as e:
        print("Something is wrong")
x = float(input("Enter number: "))
generic(x)
