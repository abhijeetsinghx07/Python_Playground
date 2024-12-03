#Write a program to check whether a given character is a special symbol or not.

value = input("Enter a character to check: ")

if len(value) == 1 and  not('a' <= value <= 'z' or 'A' <= value <= 'Z' or '0' <= value <= '9' or value == '_'):
    print(value,"is a special symbol.")

else:
    print(value,"is not special symbol.")
