##Iterators ( iter(), next() )
########### Iterable(something you can loop over (list,string,dict,tuple))
########### Iterator(the object that Does the looping, remembers its position)
#__iter__() returns the iterator object itseld
#__next__() returns the next value, raises StopIteration when done
class CountUp:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value
    
counter = CountUp(1,5)
for num in counter:
    print(num)


#EVEN NUMBERS ONLY
class EvenNumbers:
    def __init__(self, limit):
        self.current = 0
        self.limit = limit
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        value = self.current
        self.current += 2
        return value

for num in EvenNumbers(10):
    print(num)

#COUNTDOWN ITERATOR
class Countdown:
    def __init__(self,start):
        self.current = start

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value
for num in Countdown(5):
    print(num)


# range() — iterator that generates numbers
for i in range(5):
    print(i)          # 0 1 2 3 4

# enumerate() — iterator that gives index + value
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
# 0 apple
# 1 banana
# 2 cherry

# zip() — iterator that combines two lists
names  = ["Carlos", "Maria", "Ana"]
grades = [95, 87, 78]
for name, grade in zip(names, grades):
    print(f"{name}: {grade}")
# Carlos: 95
# Maria: 87
# Ana: 78

# map() and filter() — also iterators (you used these with lambdas!)
numbers = [1, 2, 3, 4, 5]
doubled = map(lambda x: x * 2, numbers)
for num in doubled:
    print(num)        # 2 4 6 8 10

