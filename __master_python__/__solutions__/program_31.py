# 31. Write a program that computes the greatest common divisor (GCD) of two positive integers.

num_1 = int(input("Enter the first value: "))
num_2 = int(input("Enter the first value: "))
num_div = []

for i in range(2,num_1+num_2):
    if num_1%i==0 and num_2%i==0:
        num_div.append(i)

print(f"Greatest Common divisor of {num_1} and {num_2} is: {num_div}")

for j in range(len(num_div)):
    if num_div[j]>num_div[j+1] and num_div[j+1]>num_div[j+2]:
        print(j)
    elif 

