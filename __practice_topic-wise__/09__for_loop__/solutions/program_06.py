#6. Write a program to reverse a string without using slicing.


value = input("Enter the string value: ")
rev   = ''

for i in value:
    rev = i+rev

print(f"Reverse if given string is : {rev}")
