
class Math:    

    @staticmethod
    def add5(x): # - cann be called without creating instance example i = Math()
        return x + 5
    
    @staticmethod
    def add3(x, y):
        return x * y

print(Math.add3(4,3))
print(Math.add5(5))

class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

print(Calculator.add(5, 4))
print(Calculator.subtract(5, 4))