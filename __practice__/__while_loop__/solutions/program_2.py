#program_2. Write a program to print the first 10 integers and their squares using a while loop take input from user.

num= int(input("Enter value to get 10 integer number with their square: "))
count= 0

while count < 10:
    
    if num:
        print("Square of integer value ",num," is ",num**2)
        
        count+=1
    
    num+=1

