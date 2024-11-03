#program_10. Write a program to check whether a number is prime or not using a while loop.

num= int(input("Enter number to check: "))
i=2

while num > 1:
    if num%i==0:
        print(num," is not a prime number.")
    i+=1

else:
    print(num,"is a prime number")