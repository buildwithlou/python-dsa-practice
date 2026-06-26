##RECURSION is like standing between two mirrors. Each mirror reflects a slightly smaller version of the scene, until the reflection gets
########### too small to see, thats your base case.

# def countdown(n): #this crashes if n is negative, because it will keep calling itself with smaller and smaller numbers forever
#     print(n)
#     countdown(n-1)


def countdown(n):
    if n == 0:
        print("Done!")
        return
    print(n)
    countdown(n - 2)


countdown(6)


def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))
print(factorial_loop(5))


# Sum of a list
def sum_list(numbers):
    if len(numbers) == 0:
        return 0
    return numbers[0] + sum_list(numbers[1:])


print(sum_list([1, 2, 3, 4, 5]))


# Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(7))
