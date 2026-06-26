def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, (exponent - 1))


print(power(2, 10))  # 1024
print(power(3, 4))  # 81
print(power(5, 0))  # 1 ← hint: anything to the power of 0 is 1
