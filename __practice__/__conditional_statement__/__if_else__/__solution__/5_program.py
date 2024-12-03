#Write a program to check whether the given string is having the middle character or not.

value = input("Enter a word to check middle value: ")

if len(value) % 2 != 0:

    print(f'"{value}" contain middle character.')
    print(f'Middle character is: "{value[round(len(value)/2)]}"')

else:
    print(f'"{value}" does not contain a middle character.')
