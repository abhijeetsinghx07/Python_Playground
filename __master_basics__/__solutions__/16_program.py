#Write a program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.

num= int(input("Enter the value: "))

diff= num-17

print(f"Difference between {num} and {17} is {diff}")

if diff>17:
    diff*=2

print(f"Twice of absolute difference: {diff}")