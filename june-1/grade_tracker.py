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

class GradeTracker:
    def __init__(self):
        self.students = {}
    
    @validate_grade
    def add_student(self, name, grade):
        self.students[name] = grade
        print(f"Added {name} with grade {grade}")
    
    def show_all(self):
        print("\n-- All Students --")
        for name, grade in self.students.items():
            print(f"{name}: {grade}")

tracker = GradeTracker()
tracker.add_student("Carlos", 95)
tracker.add_student("Maria", 87)
tracker.add_student("Ana", 101)   # should trigger decorator error
tracker.show_all()