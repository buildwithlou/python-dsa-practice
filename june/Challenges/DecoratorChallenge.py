#This decorator will check if all arguments passed to the function are positive numbers.
from functools import wraps
def validate_positive(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg <= 0:
                print("Error: all arguments must be positive")
                return None
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def calculate_area(width, height):
    return width * height

print(calculate_area(5, 4))    # should work → 15
calculate_area(-1, 3)   # should block → Error message
calculate_area(4, 0)    # should block → Error message)






