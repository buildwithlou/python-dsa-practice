#Levels of Scope LEGB (L: LOCAL), ( E: ENCLOSING), (G: GLOBAL), (B: BUILT IN)
###Local Scope: variables created inside a function, only visible inside that function
def greet():
    message = "Hello!"
    print(message)

def farewell():
    message = "Goodbye!"
    print(message)    

greet()
farewell()

###Global Scope: variables created outside all functions, visible everywhere in the file
name= "Carlos"
def greet():
    print(name)

def farewell():
    print(name)

greet()
farewell()

###Reading a global variable inside a function works fine, but modifying it requires the gloval keyword
count = 0
def increment_fixed():
    global count #it basically gives you permission to modify the variable that was declare outside the func
    count += 1

increment_fixed()
increment_fixed()
print(count)

###Enclosing Scope: when you have a function inside a function
def outer():
    message = "hello"
    def inner():
        print(message)
    inner()
outer()

def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
    inner()
    inner()
    print(count)
outer()

###Built in Scope: variables and functions Python provides automatically and you never define them
# print()
# len()
# range()
# type()
# int()
# str()
# list()

###Full Example
name = "Global Carlos"

def outer():
    name = "Enclosing Carlos"
    def inner():
        name = "Local Carlos"
        print(name)
    inner()
    print(name)
print(name)
outer()

def my_function():
    print(name)
my_function()
