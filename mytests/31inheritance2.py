# https://www.youtube.com/watch?v=pqfVGeCX5v4&list=PL7yh-TELLS1F3KytMVZRFO-xIo_S2_Jg1&index=2

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __str__(self):
        # return "X: {}, Y: {}".format(self.x, self.y)
        return f"X: {self.x}, Y: {self.y}"
    
v1 = Vector(2,3)
v2 = Vector(4,5)

print(v1)
print(v2)

v3 = v1+v2
print(v3)
v3 = v1-v2
print(v3)