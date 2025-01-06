# 7. Write a program to extract all the lowercase characters in a string only if the ascii value is even.

value = input("Enter the value: ")

for i in value:
    if 'a'<=i<= 'z' and ord(i)%2==0:
        print(i)