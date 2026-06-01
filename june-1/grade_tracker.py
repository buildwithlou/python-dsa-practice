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
        self.undo_stack = []
    
    @validate_grade
    def add_student(self, name, grade):
        self.students[name] = grade
        self.undo_stack.append(name) #push to stack
        print(f"Added {name} with grade {grade}")
    
    def show_all(self):
        print("\n-- All Students --")
        for name, grade in self.students.items():
            print(f"{name}: {grade}")

    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo")
            return
        last = self.undo_stack.pop()
        del self.students[last]
        print(f"Undid: removed {last}")

tracker = GradeTracker()
tracker.add_student("Carlos", 95)
tracker.add_student("Maria", 87)
tracker.undo()
tracker.show_all()