# 35. Write a program to check which number from 1-9 is neon number. N=9-> 9**2=81->8+1=9
    
"""(A neon number is a number where the sum of digits of square of the number is equal to the number. 
    For example if the input number is 9, its square is 9*9 = 81 and sum of the digits is 9. 
    i.e. 9 is a neon number.)"""

out = 0
neon = []
ntneon = []

for i in range(2,5000):
    out = 0
    sq = i**2
    for j in range(len(str(sq))):
        out+=sq%10
        sq//=10

    if out==i:
        neon.append(i)

    else:
        ntneon.append(i)

print(f"Neon Numbers: {neon}")

# print(f"Not-Neon Numbers{ntneon}")
        