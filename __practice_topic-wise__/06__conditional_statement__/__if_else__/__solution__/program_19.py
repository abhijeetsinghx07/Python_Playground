#Write a program to check whether a number. Entered by the user is positive or negative.

value = int(input("Enter the value to check: "))

if 0<=value<=1000:
    print("It is positive number.")

else:
    print("It is negative number.")