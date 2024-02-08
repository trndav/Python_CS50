# Tests in 38unit_test_calculator.py
def main():
    name = input("Whats your name? ")
    print(hello(name))

def hello(to="world"):
    return f"Hi, {to}"

if __name__ == "__main__":
    main()