#Write a program to check whether the given string is palindrome or not.
#A string is said to be palindrome if it remains the same on reading from both ends.

inp= input("Enter a string to check if it's a palindrome: ")

if inp == inp[::-1]:
    print("It is palindrome.")

else:
    print("It is not a palindrome ")
