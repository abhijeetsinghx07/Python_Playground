#Write a program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
'''
Sample data : 3, 5, 7, 23

Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
'''

value = input("Enter the value to convert it into list and tuple: ")

print(f"{list(value)} {tuple(value)}")