#21. Write a program to get the following output.

"""  
inp= 'haiee helloo'
Out= {"haiee':'ai', 'helloo:'eo'}
"""

inp  = input("Enter the value: ")
temp = ''
out  = {}

for i in inp:
    if i!=' ':
        temp+=i
    
    elif len(temp)%2==0:
        out[temp]=temp[1]+temp[-1]
        temp=''

    else:
        out[temp]=temp[1]+temp[2]
        temp=''
if len(temp)%2==0:
    out[temp]=temp[1]+temp[-1]
    temp=''
else:
    out[temp]=temp[1]+temp[2]
    temp=''
print(out)        

        

