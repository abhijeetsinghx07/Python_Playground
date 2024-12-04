#program_9. Write a program to print all even numbers that fall between two numbers using a while loop. 
# Take input from the user.
# Exclude both numbers.

num1= int(input("Enter the first value: "))
num2= int(input("Enter the second value: "))

if num2 <= num1: 
    print("Second value must be greater than First value")

else:
    num1+=1 #for exclude first number

    while num1 < num2:

        if num1%2==0:
            print("It is an even number: ",num1)

        num1+=1    
    
    
