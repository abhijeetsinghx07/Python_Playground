#program_11. Write a program to find the sum of the digits of a number accepted from the user.

num= int(input("Enter the value: "))
out= 0

while num > 0: 

    print("Value of num is: ",num , end=" , ")

    out = out+(num%10)
    print("Value of out after add", num%10," --> ",out)

    num = num//10
    print("Now Value of num after performing (num//10): ",num,end='\n\n')

print("The sum of the digits of a number that you given is: ", out)
