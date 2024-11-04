#program_13. Write a program to reverse the number accepted from the user using a while loop.

num= int(input("Enter the value: "))
or_num= num #variable for display original number 
out= 0      #variable to store reverse number

while num > 0:

    out = (out*10) + (num%10)

    num = num // 10

print("Reverse of number",or_num ,"is:",out)


