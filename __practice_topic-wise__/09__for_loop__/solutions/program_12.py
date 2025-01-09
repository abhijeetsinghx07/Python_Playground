# 12. Write a program to get the following output.

"""    S='power star'
    Out={'power':'rewop', 'star':'rats"}
"""

inp = input("Enter the string value: ")
out = {}
temp = ''
temp_2= ''

for i in range(0,len(inp)):
    if inp[i]!=' ':
        temp_2+=inp[i]
        temp=inp[i]+temp

    else:
        out[temp_2]=temp
        temp=''
        temp_2=''

out[temp_2]=temp    
print(f"{out}")

