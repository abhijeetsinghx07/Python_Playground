#Write a program that accepts a filename from the user and prints the extension of the file.
'''
Sample filename : abc.java
Output : java
'''

value = input("Enter your file name to extract it's extenion: ")

i=0 #initialization

while i<len(value): 
    if value[i]=='.':
        print(f"Extension is: {value[i:]}")

    i+=1 #increment


 