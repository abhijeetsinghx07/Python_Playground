# Write a program to test whether a number is within 100 of 1000 or 2000.

num= int(input("Enter the value to check: "))

if 100 <= num <= 1000:
    print(f"{num} is within 100 to 1000")

elif 1000 < num <=2000:
    print(f"{num} is within 100 to 2000")
