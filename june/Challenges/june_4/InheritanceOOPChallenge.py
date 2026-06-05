class Car:
    def __init__(self, make, model, year, speed=0):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed
    def accelerate(self, amount):
        self.speed += amount
        print(f"Speed: {self.speed}mph")
    def brake(self, amount):
        if amount > self.speed:
            print("Can't go below 0")
            return
        self.speed -= amount
        print(f"Speed: {self.speed}mph")
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
    
class Truck(Car):
    def __init__(self, make, model, year, payload):
        super().__init__(make, model, year)
        self.payload = payload
        self.cargo = 0

    def load_cargo(self, tons):
        if self.cargo + tons > self.payload:
            print("It can't exceed payload")
            return 
        self.cargo += tons
        
    def unload_cargo(self):
        self.cargo = 0
        print("The cargo is 0")

    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str}, payload: {self.payload}"
truck = Truck("Ford", "F-150", 2022, payload=2)
truck.accelerate(40)
truck.load_cargo(1.5)
truck.load_cargo(1)    
print(truck)

class SportsCar(Car):
    def __init__(self,make,model,year,turbo:bool):
        super().__init__(make,model,year)
        self.turbo = turbo
    def accelerate(self, amount):
        if self.turbo:
            amount *= 2
            print("Turbo Activated")
        super().accelerate(amount)
    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str}, Speed: {self.speed}mph, Turbo: {self.turbo}"
    
sports = SportsCar("Ferrari", "F40", 1992, turbo=True)
sports.accelerate(50)  
print(sports)