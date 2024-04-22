import matplotlib.pyplot as plt
# %matplotlib inline  

# class Circle(object):
    
#     # Constructor
#     def __init__(self, radius=3, color='blue'):
#         self.radius = radius
#         self.color = color 
    
#     # Method
#     def add_radius(self, r):
#         self.radius = self.radius + r
#         return(self.radius)
    
#     # Method
#     def drawCircle(self):
#         plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
#         plt.axis('scaled')
#         plt.show()

# RedCircle = Circle(10, 'red')
# dir(RedCircle)
# RedCircle.radius
# print(RedCircle.color)

# RedCircle.drawCircle()

# print('Radius of object:',RedCircle.radius)
# RedCircle.add_radius(2)
# print('Radius of object of after applying the method add_radius(2):',RedCircle.radius)
# RedCircle.add_radius(5)
# print('Radius of object of after applying the method add_radius(5):',RedCircle.radius)




# class Rectangle(object):
    
#     # Constructor
#     def __init__(self, width=2, height=3, color='r'):
#         self.height = height 
#         self.width = width
#         self.color = color
    
#     # Method
#     def drawRectangle(self):
#         plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
#         plt.axis('scaled')
#         plt.show()

# SkinnyBlueRectangle = Rectangle(2, 3, 'blue')
# print(SkinnyBlueRectangle.height)
# print(SkinnyBlueRectangle.width)
# print(SkinnyBlueRectangle.color)
# # SkinnyBlueRectangle.drawRectangle()

# FatYellowRectangle = Rectangle(20, 5, 'yellow')
# FatYellowRectangle.drawRectangle()




# class Car:
#     color = "white"

#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage
#         self.seat_capacity = None        

#     def seats(self, seat_capacity):
#         self.seat_capacity = seat_capacity

#     def show_all(self):
#         print(f"For this car, max speed is {self.max_speed}, mileage is: {self.mileage} and seat capacity is {self.seat_capacity}.")
        
# car1 = Car(200, 20000)
# car1.seats(5)
# car1.show_all()

# car2 = Car(180, 25000)
# car2.seats(4)
# car2.show_all()


# class Circle(object):
#     def __init__(self, radius=3, color='blue'):
#         self.radius = radius
#         self.color = color

#         # Method
#     def add_radius(self, r):
#         self.radius = self.radius + r
#         return self.radius

# C1 = Circle(4, "yellow")
# print(C1.color, C1.radius)



# class Graph():
#     def __init__(self, id):
#         self.id = id
#         self.id = 80

# val = Graph(200)
# print(val.id)



