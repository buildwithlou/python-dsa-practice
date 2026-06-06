numbers = [1,2,3,4,5]

#Old way - 3 lines
squared = []
for n in numbers:
    squared.append(n ** 2)

#List comprenhension - 1 line same result 
squared = [n ** 2 for n in numbers]

#general print
print (squared)
##The syntax for LIST COMPREHENSION: [ expression (what to do) FOR item (variable) IN iterable (the list)]

# -------------------------------------------------------------------------------------------------------------------
numbers = [1,2,3,4,5,6,7,8,9,10]

#Only even numbers
evens = [n for n in numbers if n % 2 == 0]
print(evens)

#Only numbers greater than 5 
big = [n for n in numbers if n > 5]
print(big)

#square only even numbers
squared_evens = [n ** 2 for n in numbers if n % 2 == 0]
print(squared_evens)
##The syntax for LIST COMPREHENSIONS WITH CONDITION: [ expression (what to do) FOR item (variable) IN iterable (the list) IF condition(filter)]

# -------------------------------------------------------------------------------------------------------------------
names = ["carlos", "maria", "ana", "bob"]

#Capitalize all names
capitalized = [name.capitalize() for name in names ]
print(capitalized)

#Only names longer than 3 characters
long_names = [name for name in names if len(name) > 3]
print(long_names)

#Capitalize only long names
result = [name.capitalize() for name in names if len(name) > 3]
print(result)

# -------------------------------------------------------------------------------------------------------------------
students = [
    {"name": "Carlos", "grade": 95},
    {"name": "Maria",  "grade": 72},
    {"name": "Ana",    "grade": 88},
    {"name": "Bob",    "grade": 65},
]

#Get just the names but in general is calling the object the you are telling you either can change "name" for "grade"
names = [s["name"] for s in students]
print(names)

#Get names of passing students only
passing = [s["name"] for s in students if s["grade"] >= 75]
print(passing)

#Add letter grade to each student
graded = [{**s, "letter": "A" if s["grade"] >= 90 else "B" if s["grade"] >= 80 else "C"} for s in students] 
for s in graded:
    print(f"{s['name']}: {s['letter']}")
##Working with dictionaries

# -------------------------------------------------------------------------------------------------------------------
numbers = [1,2,3,4,5]

squares_dict = {n: n**2 for n in numbers}
print(squares_dict)
##Dictionary comprehension

# -------------------------------------------------------------------------------------------------------------------
words = ["hello", "world", "hello", "python", "world"]
unique = {word for word in words}
print(unique)
##Set comprehension (removing the duplicates automatically)

# -------------------------------------------------------------------------------------------------------------------
matrix = [[1,2,3], [4,5,6], [7,8,9]]
flat = [num for row in matrix for num in row]
print(flat)

# -------------------------------------------------------------------------------------------------------------------
numbers = [1,2,3,4,5]

squared = list(map(lambda x: x**2, numbers))
#map + lambda

squared = [x**2 for x in numbers]
#list comprehension - more readable 


evens = list(filter(lambda x:x %2 == 0, numbers))
#filter + lambda

evens = [x for x in numbers if x % 2 == 0]
#list comprehension - more readable

# # Basic
# [expression for item in list]

# # With filter
# [expression for item in list if condition]

# # Dictionary comprehension
# {key: value for item in list}

# # Set comprehension
# {expression for item in list}

# # Nested
# [expression for outer in list for inner in outer]




