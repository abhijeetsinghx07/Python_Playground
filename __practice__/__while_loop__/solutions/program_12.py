#program_12. Write a program to find the product of the digits of a number accepted from the user.

num= int(input("Enter the value: "))
out= 1

while num > 0 :

    out = out * (num%10)

    num = num // 10

print("Product of the digits of a number given by you is: ",out)