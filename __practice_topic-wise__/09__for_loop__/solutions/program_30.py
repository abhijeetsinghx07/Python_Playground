# 30. Write a program to check whether the number is neon number or not. N=9-> 9**2=81->8+1=9
    
"""(A neon number is a number where the sum of digits of square of the number is equal to the number. 
    For example if the input number is 9, its square is 9*9 = 81 and sum of the digits is 9. 
    i.e. 9 is a neon number.)"""

num = int(input("Enter the value: "))
sq  = num**2
out = 0

for i in range(len(str(sq))):
    print('SQ:',sq)
    out+=sq%10
    print('out:', out)
    sq//=10
    print('sq:',sq)

if out==num:
    print("It is a neon number.")

else:
    print("It is not a neon number.")
   