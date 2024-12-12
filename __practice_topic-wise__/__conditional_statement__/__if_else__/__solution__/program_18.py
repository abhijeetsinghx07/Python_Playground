# Write a program to find the largest number out of two numbers expected from the user.

num1= int(input("Enter the value to check : "))
num2= int(input("Enter the value to check : "))

if num1 > num2:
    print(f"First value: {num1} is greater than second value: {num2}")

else:
    print(f"Second value: {num2} is greater than first value: {num1}")