#Write a program to consider an integer number. 
#If the number is even then print square of the number else print the cube of the number.

num = int(input("Enter the value to check: "))

if num%2==0:
    print(f"Square of given number '{num}' is: {num**2}")

else:
    print(f"Cube of given number '{num}' is: {num**3}")