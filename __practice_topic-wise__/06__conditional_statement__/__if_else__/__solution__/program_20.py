#Write a program to check whether a number accepted from the user is divisible by two and three both.

value= int(input("Enter the value to check: "))

if value%2==0 and value%3==0:
    print(f"Entered value {value} is divisible by both 2 and 3.")

else:
    print(f"Entered value {value} is not divisible by both 2 and 3.")