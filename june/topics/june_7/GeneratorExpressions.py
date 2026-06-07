###GENERATOR EXPRESSION: creates values one at a time, only when needed using ()
numbers = (x**2 for x in range(4))
print(numbers)

print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))


import sys

# List — stores everything in memory at once
numbers_list = [x**2 for x in range(100000)]
print(sys.getsizeof(numbers_list))   # ~800,000 bytes (800KB!)

# Generator — stores almost nothing
numbers_gen = (x**2 for x in range(100000))
print(sys.getsizeof(numbers_gen))    # ~200 bytes (tiny!)

gen = (x**2 for x in range(5))
for num in gen:
    print(num)

gen = (x**2 for x in range(5))
list1 = list(gen)
list2 = list(gen)
print(list1)
print(list2)

def generate_numbers():
    yield 1
    yield 2
    yield 3
gen = generate_numbers()
print(next(gen))
print(next(gen))
print(next(gen))

def count_up(start, end):
    current = start
    while current <= end:
        yield current #yield pause and return a value 
        current += 1
counter = count_up(1,5)
for num in counter:
    print(num)

for num in range(1,6):
    print(num)


##processes one line at a time
# def read_large_file(filename):
#     with open(filename) as f:
#         for line in f:
#             yield line.strip()

# for line in read_large_file("huge_file.txt"):
#     print(line)

##Infinite sequences
def infinite_counter(start=0):
    current = start
    while True:
        yield current
        current += 1
counter = infinite_counter()
print(next(counter))
print(next(counter))
print(next(counter))

##Fibonacci with generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
fib = fibonacci()

for _ in range(10):
    print(next(fib), end= " ")

##Generator work perfectly with sum(), max(), min(), list()
#Sum a million numbers without storing them all
total = sum(x**2 for x in range(1000000))
print(f"\n{total}")

#Find max without storing the list
biggest = max(x**2 for x in range(100))
print(biggest)

#Convert to list when you need all values
squares = list(x**2 for x in range(10))
print(squares)



