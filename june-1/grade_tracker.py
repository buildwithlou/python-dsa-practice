#Student Grade Tracker
#Topics: Decorators, HashMaps, Linked List, Stack, BST
def validate_grade(func):
    def wrapper(*args, **kwargs):
        #args[2] will be the grade
        if args[2] < 0 or args[2] > 100:
            print("ERROR: grade must be between 0 and 100")
            return None
        return func(*args, **kwargs)
    return wrapper

