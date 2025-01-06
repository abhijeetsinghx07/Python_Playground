# 31. Write a program that computes the greatest common divisor (GCD) of two positive integers.

num_1 = int(input("Enter the first value: "))
num_2 = int(input("Enter the first value: "))
num_div = []

for i in range(2,num_1+num_2):
    if num_1%i==0 and num_2%i==0:
        num_div.append(i)

print(f"Greatest Common divisor of {num_1} and {num_2} is: {num_div}")