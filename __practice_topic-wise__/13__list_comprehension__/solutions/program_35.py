# 35. Create a list of booleans indicating whether numbers from 1 to 10 are even.

numbers = [True if i % 2 == 0 else False for i in range(1,11) ]

print(numbers)