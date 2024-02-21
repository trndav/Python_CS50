
class Point():
    def __init__(self, x=0, y=0):
        self.x = x 
        self.y = y 
        self.coords = (self.x, self.y)

    def move(self, x, y):
        self.x += x
        self.y += y

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, p):
        return self.x * p.x + self.y * p.y

    def __str__(self):
        return "(" + str(self.x) + ',' + str(self.y) + ')'

    def length(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)

    # def __len__(self):
    #     import math
    #     return math.sqrt(self.x**2 + self.y**2)

    def __gt__(self, p): # Greater than
        return self.length() > p.length()

    def __ge__(self, p): # Greater equal
        return self.length() >= p.length()

    def __lt__(self, p): # Less than
        return self.length() < p.length()

    def __le__(self, p): # Less equal
        return self.length() <= p.length()

    def __eq__(self, p): # Equal
        return self.x == p.x and self.y == p.y
    
p1 = Point(3,4)
p2 = Point(3,4)
p3 = Point(1,3)
p4 = Point(0,1)
# p5 = p1 + p2 
# p6 = p4 - p1
# p7 = p2 * p3 

# print(p5, p6, p7)
print(p1 == p2)
print(p1.__eq__(p2))
print(p1 > p2)
print(p4 <= p3)