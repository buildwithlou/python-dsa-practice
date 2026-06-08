#Context Manager is a construct that allows you to set up and clean up no matter what happens, even if the code crashes
##works with __enter__() {setup} and __exit__() {cleanup}
# with open("tasks.json") as f:
#     content = f.read() #file closes automatically here, even if an error occurred
###behind the scenes looks like this:
# f = open("tasks.json")
# f.__enter__()
# try:
#     content = f.read()
# finally:
#     f.__exit__()

#Reading a file
# with open("tasks.json", "r") as f:
#     content = f.read()

#Writing a file
# with open("tasks.json", "w") as f:
#     f.write("Hello World")

#Multiple files at once
# with open("input.txt", "r") as inp, open("output.txt", "w") as out:
#     content = inp.read()
#     out.write(content.upper())

#Database connections
# with get_database_connection() as db:
#     db.execute("SELECT * FROM users")

###Using classes
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        print("Timer started")
        return self
    
    def __exit__(self, exc_type, exc_val, exe_tb): #exc_type: error type, exc_val: error msg, exc_tb: traceback
        import time
        end = time.time()
        print(f"Time elapsed: {end - self.start: .4f} seconds")
        return False

with Timer() as t:
    total = sum(x**2 for x in range(1000000))

###Using contextlib (generators)
from contextlib import contextmanager
@contextmanager
def timer():
    import time
    start = time.time()
    print("Timer started")
    yield  #splits the function into setup and cleanup, much cleaner than writing a full class

    end = time.time()
    print(f"Time elapsed: {end - start:.4f} seconds")
with timer():
    total = sum(x**2 for x in range(1000000))

###Managed file writing
from contextlib import contextmanager

@contextmanager
def managed_file(filename):
    print(f"Opening {filename}")
    f = open(filename, "w")
    try: 
        yield f
    finally:
        f.close()
        print(f"Closed {filename}")
with managed_file("test.txt") as f:
    f.write("Hello World")

###Database transaction
from contextlib import contextmanager
@contextmanager
def transaction(db):
    try: 
        yield db    #run the code inside with block
        db.commit() #if no error, then save changes
        print("Transaction committed")
    except Exception as e:
        db.rollback() #if error, then undo changes
        print(f"Transaction rolled back {e}")

###Temporary directory
from contextlib import contextmanager
import os
@contextmanager
def temp_directory(name):
    os.mkdir(name)
    print(f"Created {name}")
    try: 
        yield name
    finally:
        os.rmdir(name)
        print(f"Deleted {name}")
with temp_directory("temp_work") as folder:
    print(f"Working in {folder}")

###Error handling in context managers
from contextlib import contextmanager
@contextmanager
def safe_open(filename):
    try:
        f = open(filename)
        yield f
    except FileNotFoundError:
        print(f"File {filename} not found!")
        yield None
    finally:
        print("Done with file operation")
    
with safe_open("missing.txt") as f:
    if f:
        print(f.read())

