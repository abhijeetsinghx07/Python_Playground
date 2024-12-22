#Write a program to check whether the user is eligible to vote or not.

age= int(input("Enter your age to check elgibility: "))

if age >= 18:
    print("You are eligible to vote.")

else:
    print("You are not eligible to vote.")
    print(f"Try after {18-age} year.")