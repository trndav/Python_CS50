class Vector:
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    # def __str__(self):
    #     return str(self.name) + ", " + str(self.age)
    # Or 
    
    def __repr__(self):
        return f"X: {self.x}, Y: {self.y}"
    
    def __call__(self):
        print("Hei, call!")
    
v1 = Vector(10,15)
v2 = Vector(33, 44)
v3 = v1 + v2
v3() # Call method
print(v3)
print(v3.y)