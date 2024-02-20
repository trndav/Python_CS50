class Vehicle():
    def __init__(self, price, gas, color):
        self.price = price
        self.gas = gas
        self.color = color
    
    def fillTank(self):
        self.gas = 100

    def emptyTank(self):
        self.gas = 0

    def gasLeft(self):
        return self.gas


class Car(Vehicle):
    def __init__(self, name, price, gas, color, speed):
        super().__init__(price, gas, color)
        self.name = name
        self.speed = speed
    
    def beep(self):
        print("Beep! Beep!")

    def specs(self):
        return (self.name, self.price, self.gas, self.color, self.speed)


class Truck(Vehicle):
    def __init__(self, price, gas, color, speed):
        super().__init__(price, gas, color)
        self.tires = tires
    
    def beep(self):
        print("Honk! Honk!")

car = Car("Mercedes", 12000, "Diesel", "Grey", 200)
print(car.specs())