numbers = range(1, 1001)
# Create a generator for all odd numbers in the range
oddNumbers = (x for x in range(1, 1001) if x % 2 != 0)
print("-----------------ALL ODD NUMBERS IN THE RANGE-----------------")
for x in oddNumbers:
    print(x, end=" ")
# Create a generator for the squares of even numbers only
squareNumbers = (x**2 for x in numbers if x % 2 == 0)
print("\n\n-----------------ALL SQUARES OF EVEN NUMBERS-----------------")
for x in squareNumbers:
    print(x, end=" ")
# Use sum() with a generator to find the total of all numbers divisible by 3
sumNumbers = sum(x for x in numbers if x % 3 == 0)
print("\n\n-----------------SUM OF ALL NUMBERS DIVISIBLE BY 3-----------------")
print(sumNumbers)
# Use max() with a generator to find the largest odd number under 1000
maxNumber = max(x for x in numbers if x % 2 != 0)
print("\n\n-----------------MAX OF ALL NUMBERS-----------------")
print(maxNumber)
