# 36. Write a program to add two objects if both objects are integers.

num_1 = int(input("Enter the first value: "))
num_2 = int(input("Enter the second value: "))

if type(num_1)==int and type(num_2)==int:
    print(f"Sum of {num_1} and {num_2} is : {num_1+num_2}")

