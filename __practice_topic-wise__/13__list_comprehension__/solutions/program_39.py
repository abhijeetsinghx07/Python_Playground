# 39. Generate a list of all two-digit numbers divisible by 11.

number = [i for i in range(1,100) if 10<=i<=99 and i % 11 == 0]

print(number)