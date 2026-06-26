student1_name = "Carlos"
student1_age = 20
student1_grade = 95

student2_name = "Lourdes"
student2_age = 25
student2_grade = 100


###Classes let you create a blueprint(plan or template for creating something) and stamp out as many copies as you need
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self):
        print(f"Hi I'm {self.name}, I'm {self.age} years old")

    def is_passing(self):
        return self.grade >= 60

    def get_letter_grade(self):
        if self.grade >= 90:
            return "A"
        elif self.grade >= 80:
            return "B"
        elif self.grade >= 70:
            return "C"
        else:
            return "F"

    def __str__(self):
        return f"Student({self.name}, age{self.age}, grade{self.grade})"


# With classes — clean
student1 = Student("Carlos", 20, 95)
student2 = Student("Lourdes", 25, 100)
student3 = Student("William", 28, 59)
# 100 students? no problem
print(student3)
student3.grade = 99
print(student3.grade)
print(student2.is_passing())
print(student2.get_letter_grade())


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
            return
        self.balance -= amount
        print(f"Withdrew ${amount}. Balance: ${self.balance}")

    def show_balance(self):
        print(f"{self.owner}'s balance: ${self.balance}")


# Create two independent accounts
willisito_account = BankAccount("Willisito", 100000)
lourdes_account = BankAccount("Lourdes", 20000)
willisito_account.deposit(1000)
willisito_account.withdraw(10)
lourdes_account.withdraw(100)
lourdes_account.show_balance()
