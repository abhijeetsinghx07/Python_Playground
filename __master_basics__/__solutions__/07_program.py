#Write a program that accepts a filename from the user and prints the extension of the file.
'''
Sample filename : abc.java
Output : java
'''

value = input("Enter your file name to extract it's extenion: ")

ext=value.split('.')

print(f"Your Extension is : {ext[-1]}")



 