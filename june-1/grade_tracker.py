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

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class ActionLog:
    def __init__(self):
        self.head = None
    
    def log(self, action):
        new_node = Node(action)
        new_node.next = self.head
        self.head = new_node

    def show_log(self):
        print("\n--- Action Log---")
        current = self.head
        while current:
            print(f"→ {current.value}")
            current = current.next

class GradeTracker:
    def __init__(self):
        self.students = {}
        self.undo_stack = []
        self.log = ActionLog() 
    
    @validate_grade
    def add_student(self, name, grade):
        self.students[name] = grade
        self.undo_stack.append(name) #push to stack
        self.log.log(f"Added {name} with grade {grade}")
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
        self.log.log(f"Undid: removed {last}")
        print(f"Undid: removed {last}")

tracker = GradeTracker()
tracker.add_student("Carlos", 95)
tracker.add_student("Maria", 87)
tracker.add_student("Ana", 78)
tracker.undo()
tracker.log.show_log()    # should show all actions, latest first
tracker.show_all()