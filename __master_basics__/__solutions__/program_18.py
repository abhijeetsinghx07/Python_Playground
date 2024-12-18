#Write a program to calculate the sum of three given numbers. If the values are equal, return three times their sum.

num1= int(input("Enter the first value: "))
num2= int(input("Enter the second value: "))
num3= int(input("Enter the third value: "))

sum=num1+num2+num3

if num1==num2==num3:
    sum*=3

print(f"Three times of sum: {sum}")
