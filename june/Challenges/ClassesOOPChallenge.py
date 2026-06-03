class Car:
    def __init__(self, make, model, year, speed=0):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed
    def accelerate(self, amount):
        self.speed += amount
        print(self.speed)
    def brake(self, amount):
        if amount > self.speed:
            print("Can't go below 0")
            return
        self.speed -= amount
        print(self.speed)
    def show_status(self):
        print(f"{self.make} {self.model} {self.year} - Speed: {self.speed}mph ")
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

car1 = Car("Toyota", "Corolla", 2020)
car1.accelerate(30)
car1.accelerate(20)
car1.brake(10)
car1.show_status()
print(car1)