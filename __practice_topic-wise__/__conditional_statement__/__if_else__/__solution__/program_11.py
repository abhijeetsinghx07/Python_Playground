#Write a program to check whether the given string is palindrome or not.

inp= input("Enter a strind to check: ")

if inp[0:] == inp[::-1]:
    print("It is palindrome.")

else:
    print("It is not a palindrome ")
