#Write a program to check whether the given 2 variables are pointing to the same memory location or not.

var1= int(input("Enter first number: "))

var2= int(input("Enter second number: "))

if id(var1) == id(var2):
    print(f"{var1} and {var2} both have same memory location.")

else:
    print(f"{var1} and {var2} both have different memory location.")