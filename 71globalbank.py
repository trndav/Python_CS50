# global variables
# Can read global variable, but cant write to global var

# balance = 0 # global balance used in deposit and withdraw

# def main():
#     print("Balance", balance)
#     deposit(100)
#     withdraw(50)
#     print("Balance", balance)

# def deposit(n):
#     global balance
#     balance += n 

# def withdraw(n):
#     global balance
#     balance -= n

# if __name__=="__main__":
#     main()

# Instead of global var, we can use classes with global self variables
class Account:
    def __init__(self):
        self._balance = 0  # private ? not really
    
    @property # Property is instance variable that is protected
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n 
    
    def withdraw(self, n):
        self._balance -= n 

def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)
        
if __name__ == "__main__":
    main()