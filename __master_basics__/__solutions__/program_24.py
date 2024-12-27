#Write a program to test whether a passed letter is a vowel or not.

value = input("Enter the letter from A to Z: ")

if value in 'aeiouAEIOU':
    print(f"{value} is a vowel.")

else:
    print(f"{value} is not a vowel.")

