# Error or exception

# Syntax error
# a = 5 print(a)
# print(a))

# a = 5
# b = c

# nameerror
# File not found error
# Valueerror
# Indexerror
# Keyerror


# a = [1, 2, 3]
# a.remove(4)
# print(a)

# x = -5
# # if x < 0:
# #     raise Exception("X should be positive")
# assert (x>=0), "x must be positive"

# try: 
#     a = 5 / 0
# except Exception as e:
#     print(f"Error happened: {e}")

try: 
    a = 5 / 1
    b = a + 10
except ZeroDivisionError as e:
    print(f"Error happened: {e}")
except TypeError as t:
    print(f"Error happened: {t}")
else:
    print("Everything is fine.")
finally:
    print("Cleaning up...")

print("*" * 9)

class ValueTooHighError(Exception):
    pass
class ValueTooLowError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError("Value is too high")
    if x < 5:
        raise ValueTooLowError("Value is too small", x)

try: 
    test_value(4)
except ValueTooHighError as e:
    print(f"Error: {e}")
except ValueTooLowError as e:
    print(f"Error: {e.message}, value: {e.value}")