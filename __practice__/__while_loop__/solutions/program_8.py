#program_8. Write a program to print a table of a number entered from the user.

num= int(input("Enter any number to get Multiplication Table: "))
till= int(input("How many multiples of the number you want: ")) 
i= 1

print("Table of:",num,"\n")

while i <= till:
    
    print(num,"*",i,"-->", num*i)

    i+=1 #increment by 1

