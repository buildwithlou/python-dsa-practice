##Decoratos are functions that modify the behavior of other functions without changing their code.

# 1.Function are just values, You can store them, pass them, return them.
def greet():
    print("Hello!")


# Store in a variable
say_hello = greet
say_hello()


# Pass as argument
def run(func):
    func()


run(greet)  # It will print: "Hello!"


# Return from another function
def get_greeter():
    return greet


fn = get_greeter()
fn()


# 2.Functions inside functions, the inner function only exists inside outer. thid id called a closure.
def outer():
    def inner():
        print("I'm inside outer!")

    inner()


outer()  # I am inside outer!


# 3.A decorator is a function that takes a function as input, wraps it with extra behavior, returns the new wrapped function.
def my_decorator(func):  # Takes a function as input
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")

    return wrapper


def say_hello():
    print("Hello!")


say_hello = my_decorator(say_hello)
say_hello()


# 4.The @ Syntax is a shortcut for applying a decorator to a function to replace the "say_hello = my_decorator(say_hello)" line.
def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")

    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()


# 5.For future decorator with arguments
def my_decorator(func):
    def wrapper(
        *args, **kwargs
    ):  # this two arguments allow to pass any number of positional and keyword arguments to the original function. even just one or none.
        print("Before the function runs")
        result = func(*args, **kwargs)
        print("After the function runs")
        return result

    return wrapper


@my_decorator
def add(a, b):
    return a + b


print(add(3, 4))
