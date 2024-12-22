#Write a program to check whether a number entered is a 3 digit number or not.
#Without using type casting.

num= int(input("Enter 3 digit number: "))

if 100 <= num <=999 or -999 <= num <= -100  :
    print(f"{num} is a three digit number.")

else:
    print(f"{num} is not three digit number.")