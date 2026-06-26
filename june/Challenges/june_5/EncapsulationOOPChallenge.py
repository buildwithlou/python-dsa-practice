class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.__age = age
        self.__email = email

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0 or value > 120:
            print("Error: Invalid age. Must be between 0 and 120")
            return
        self.__age = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if "@" not in value:
            print("Error: Invalid email. Must include @")
            return
        self.__email = value

    def __str__(self):
        return f"{self.name} ({self.__age}) - {self.__email}"


p = Person("Carlos", 25, "carlos@gmail.com")
print(p)  # Carlos (25) - carlos@gmail.com

p.age = 30  # valid
p.age = -5  # Error: invalid age
p.age = 150  # Error: invalid age

p.email = "newemail@gmail.com"  # valid
p.email = "notanemail"  # Error: invalid email

print(p.age)  # 30
print(p.email)  # newemail@gmail.com
print(p)
