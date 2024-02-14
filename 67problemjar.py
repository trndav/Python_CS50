class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        cookie = "🍪"
        multi = self._size * cookie
        return f"{multi}"

    def deposit(self, n):
        if n < 0:
            raise ValueError
        total_cookies = self._size + n
        if total_cookies > self.capacity:
            raise ValueError("Exceeds jar capacity")
        self._size = total_cookies
        return self

    def withdraw(self, n):
        if n > self._size:
            raise ValueError("Jar does not have that many cookies")
        balance = self._size - n
        self._size = balance
        return self

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not capacity:
            raise ValueError("Missing capacity")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if not size:
            raise ValueError("Missing size")
        self._size = 0

# jar = Jar()
# jar.deposit(2)
# print(f"Balance: {jar}")

# jar.withdraw(1)
# print(f"Balance: {jar}")

