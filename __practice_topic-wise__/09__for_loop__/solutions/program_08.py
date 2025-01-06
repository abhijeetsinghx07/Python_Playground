# 8. Write a program to check whether all digits of an integer is even or odd.

value = int(input("Enter the value: "))
temp = 0

for i in range(0,len(str(value))):
   
    temp = value%10

    if temp%2==0:
        print(f"{temp} is even.")
    
    else:
        print(f"{temp} is odd.")

    value //= 10
    temp=0