#Write a program to consider string input, 
#if it is having more than three characters then print length of the string else print string as it is.

inp= input("Enter the string: ")


if len(inp) > 3:
    print(f"Lenght of give string is {len(inp)}")

else:
    print(f"Your given string have less than three character : '{inp}' ")