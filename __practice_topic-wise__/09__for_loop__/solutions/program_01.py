# 1. Write a program to find the product of all the digits present in a number.

value= int(input("Enter the value: "))
out= 1

for i in range(0,len(str(value))):
    out = out*(value%10)

    value//=10

print(out)