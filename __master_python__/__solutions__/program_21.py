#Write a program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.

value= int(input("Enter value here: "))

if value%2==0:
    print(f"{value} is an even number.")

else:
    print(f"{value} is an odd number.")