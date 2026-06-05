###ENCAPSULATION: use to hide the internal workings, expose only what the user needs. thats why encapsulation uses underscores
class Student:
    def __init__(self,name, grade):
        self.name = name     #public (anyone can access)
        self._grade = grade  #protected (intended for internal use)
        self.__id = "S001"   #private (truly hidden)

s = Student("Carlos", 95)
print(s.name)     #is going to print the name
print(s._grade)   #print is protected
#print(s.__id)   #is going to show an error the only way to access it is printing s._Student__id

###Getters and Setters (Since private attributes are hidden, you control access through methods)
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    #GETTER - controlled READ access
    def get_balance(self):
        return self.__balance
    #SETTER - controlled WRITE access with validation
    def set_balance(self,amount):
        if amount < 0:
            print("Balance can't be negative")
            return
        self.__balance = amount
    def deposit(self,amount):
        if amount <= 0:
            print("Deposit must be positive")
            return
        self.__balance += amount
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds")
            return
        self.__balance -= amount
        print(f"Withdrew ${amount}. Balance: ${self.__balance}")
account = BankAccount("Carlos", 1000)
print(account.get_balance())
account.set_balance(-500)
account.deposit(200)
account.withdraw(2000)
print(account.get_balance())

#Python has a cleaner way to do getters and setters using @property
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    @property #let you use account.balance instead of account.get_balance()
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Balance can't be negative")
            return
        self.__balance = amount
account = BankAccount("Carlos", 1000)

print(account.balance)
account.balance = 2000
account.balance = -500
print(account.balance)

#Sometimes you want data that can be read but never changed
class Circle:
    def __init__(self,radius):
        self.__radius = radius
    @property
    def radius(self):
        return self.__radius
    @property
    def area(self):
        import math
        return round(math.pi + self.__radius ** 2, 2)
    @property
    def diameter(self):
        return self.__radius * 2
circle = Circle(5)
print(circle.radius)
print(circle.area)
print(circle.diameter)
# circle.area = 100. #read only, no setter defined

class Student:
    def __init__(self,name,grade):
        self.name = name
        self.__grade = grade
    @property
    def grade(self):
        return self.__grade
    @grade.setter
    def grade(self, value):
        if value < 0 or value > 100:
            print("Grade must be between 0 and 100")
            return
        self.__grade = value
    @property
    def letter_grade(self):
        if self.__grade >= 90:
            return "A"
        elif self.__grade >= 80:
            return "B"
        elif self.__grade >= 70:
            return "C"
        else:
            return "F"
    def __str__(self):
        return f"{self.name}: {self.__grade} ({self.letter_grade})"
s = Student("Carlos", 95)
print(s)
s.grade = 85
print(s)
s.grade = 150
s.grade = -10
print(s.letter_grade)