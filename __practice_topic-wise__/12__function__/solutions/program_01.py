# 1. Wap to check whether the number is strong or not. 

""" Strong number is a special number whose sum of the factorial of digits is equal to the original number. 
For Example: 145 is strong number. 
1! + 4! + 5! = 145. 
1 + (4*3*2*1) + (5*4*3*2*1) = 145 """

def StrongNumber(num,sum=0):
    temp = num
    for i in range(0,len(str(num))):
        digit = temp % 10
        fact = 1
        while digit != 0:
            fact *= digit
            digit -= 1
        sum += fact
        temp //= 10

    if num == sum:
        return f"{num} is an strong number."

print(StrongNumber(int(input("Enter the value: "))))