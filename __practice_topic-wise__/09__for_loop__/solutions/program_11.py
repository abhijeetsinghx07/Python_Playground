# 11. Write a program to get the following output using len function.
"""
S='power star'

Out={'power':5, 'star':4}

"""  

inp = input("Enter the string value: ")
temp= ''
count= 0
out = {}

for i in range(0,len(inp)):
    if inp[i]!=' ':
        temp+=inp[i]
        count+=1
    else:
        out[temp]=count
        temp=''
        count=0

out[temp]=count
print(f"{out}")
