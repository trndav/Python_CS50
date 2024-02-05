def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    var = d.replace("$", "")
    return float(var)

def percent_to_float(p):
    var2 = p.replace("%", "")
    return float(var2)/100

main()