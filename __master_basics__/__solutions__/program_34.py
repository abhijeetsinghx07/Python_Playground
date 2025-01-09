# 34. Write a program to sum two given integers. 
# However, if the sum is between 15 and 20 it will return 20.

num_1 = int(input("Enter the first value: "))
num_2 = int(input("Enter the second value: "))


if 15<=num_1+num_2<=20:
    print(f"Sum of {num_1} and {num_2} is between 15 and 20 so output is: {20}")

else:
    print(f"Sum of {num_1} and {num_2} is: {num_1+num_2}")
