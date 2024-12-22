#Write a program to check whether the given string is having the middle character or not.

value = input("Enter a word to check middle value: ")

#only odd length string have middle character 

if len(value) % 2 != 0:            
    
    middle_index = len(value)//2  #calculate the middle character here

    print(f'"{value}" contain middle character.')
    print(f'Middle character is: "{value[middle_index]}"')

else:
    print(f'"{value}" does not contain a middle character.')
