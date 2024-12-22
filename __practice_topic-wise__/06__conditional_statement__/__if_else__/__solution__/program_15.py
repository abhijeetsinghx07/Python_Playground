#Write a program to check whether the last digit of a number entered by the user is divisible by three or not.

inp= int(input("Enter the value to check: "))
ld= inp%10

if ld % 3 == 0:
    print(f"Entered value {inp} last digit {inp%10} is divisible by 3.")

else:
    print(f"Entered value {inp} last digit {inp%10} is not divisible by 3.")