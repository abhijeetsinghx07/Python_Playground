# Write a program to get n copies of the first 2 characters of a given string. 
# Return n copies of the whole string if the length is less than 2.

value = input("Enter the string: ")
n = int(input("How many copy you want: "))

if len(value)>2:
    print(value[:2]*n)

else:
    print(value*n)

