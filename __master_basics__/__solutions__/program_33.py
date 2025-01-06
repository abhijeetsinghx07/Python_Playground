# 33. Write a program to sum three given integers. However, if two values are equal, the sum will be zero.


num_1 = int(input("Enter the first value: "))
num_2 = int(input("Enter the second value: "))
num_3 = int(input("Enter the third value: "))

if num_1!=num_2:
    print(f"Sum of {num_1} and {num_2} is: {num_1+num_2+num_3} ")

else:
    print(f"Sum of {num_1} {num_2} and {num_3} is: 0 ")