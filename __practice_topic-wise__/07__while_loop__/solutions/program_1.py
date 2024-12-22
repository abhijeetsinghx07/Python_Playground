# program_1. Write a program to print first 10 even number using while loop take input from user


num= int(input("Enter value to get 10 even number: "))
i= num
count= 0

while count < 10:

    if i % 2 == 0:
        print(i, "is an even number.") 
        count+=1

    i+=1




