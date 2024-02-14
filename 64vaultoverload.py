# class Vault:
#     def __init__(self, galleons=0, sickles=0, knuts=0):
#         self.galleons = galleons 
#         self.sickles = sickles
#         self.knuts = knuts
#     def __str__(self):
#         return f"{self.galleons} galleons, {self.sickles} sickles, {self.knuts} knuts."

# potter = Vault(100, 50, 25)
# print(f"Potter balance: {potter}")

# weasly = Vault(25, 50, 100)
# print(f"Weasly balance: {weasly}")

# galleons = potter.galleons + weasly.galleons
# sickles = potter.sickles + weasly.sickles
# knuts = potter.knuts + weasly.knuts
# total = Vault(galleons, sickles, knuts)
# print(total)

# Overloaded operator
class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons 
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} galleons, {self.sickles} sickles, {self.knuts} knuts."

    # Overloaded operator
    def __add__(self, other):  # self left from + other right from + +-*/
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)

potter = Vault(100, 50, 25)
print(f"Potter balance: {potter}")
weasly = Vault(25, 50, 100)
print(f"Weasly balance: {weasly}")

total = potter + weasly # ? goes to __add__(self, other)
print(total)