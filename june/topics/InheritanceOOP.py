#Inheritance: is when yo inherits everything from Car; (ClassesOOPChallenge)
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


class ElectricCar(Car):
    def __init__(self,make,model,year,battery=100):
        super().__init__(make,model,year)
        self.battery = battery

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
    def __str__(self):
        return f"{self.name}, age{self.age}"
    
class Dog(Animal):
    def bark(self):
        print(f"{self.name} says: Woof!")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} says: Meow!")

dog= Dog("Rex", 3)
cat= Cat("Whiskers", 5)

dog.eat()
dog.sleep()
dog.bark()

cat.eat()
cat.meow()

print(dog)

##using super() lets you call the parent's method from the child:
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Dog(Animal):
    def __init__(self,name,age,breed):
        super().__init__(name,age)
        self.breed = breed

dog = Dog("Rex", 3, "Labrador")
print(dog.name)
print(dog.age)
print(dog.breed)

class Animal:
    def speak(self):
        print("some generic animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Duck(Animal):
    def speak(self):
        print("Quack!")

animals = [Dog("Rex", 3), Cat("Whiskers", 5), Duck("Donald", 2)]
for animal in animals:
    animal.speak()

##Sometimes you dont want to fully replace a parent method just add to it
class Animal:
    def __str__(self):
        return f"{self.name}, age {self.age}"

class Dog(Animal):
    def __init__(self,name,age,breed):
        super().__init__(name, age)
        self.breed = breed
    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str}, breed: {self.breed}"
    
dog = Dog("Rex", 3, "Labrador")
print(dog)

###Inheritance can go multiple levels deep:
class Animal:
    def __init__(self, name):
        self.name = name
    def breathe(self):
        print(f"{self.name} is breathing")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks")
    
class GuideDog(Dog):
    def guide(self):
        print(f"{self.name} is guiding its owner")
    
guide_dog = GuideDog("Buddy")
guide_dog.breathe()
guide_dog.bark()
guide_dog.guide()

###Back to your Car class from the Classes OOP Challenge
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

    def __str__(self)    :
        return f"{self.year} {self.make} {self.model}"
    
class ElectricCar(Car):
    def __init__(self, make, model, year, battery=100):
        super().__init__(make, model, year)
        self.battery = battery
    def charge(self):
        self.battery = 100
        print("Fully charged!")
    def accelerate(self, amount):
        if self.battery <= 0:
            print("No battery left!")
            return
        super().accelerate(amount)
        self.battery -= 10
        print(f"Battery: {self.battery}%")
    def __str__(self):
        return f"{super().__str__()} (Electric)"
    
tesla = ElectricCar("Tesla", "Model 3", 2023)
tesla.accelerate(30)
tesla.accelerate(20)
tesla.brake(10)
tesla.charge()
print(tesla)

dog = Dog("Rex", 3, "Labrador")
print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(isinstance(dog, Cat))

