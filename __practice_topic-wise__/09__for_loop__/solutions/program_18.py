# 18. Write a program to get the following output.
""" 
Inp='push maadi kushi padi'
Out={'push': 'ph', 'maadi': 'a', 'kushi':'s', 'padi':'pi"}   
"""

inp ='push maadi kushi padi'
out = {}
temp = ''

for i in inp:
    if i!=' ':
        temp+=i
    
    elif len(temp)%2==0:
        out[temp] = temp[0]+temp[-1]
        temp=''

    else:
        out[temp] = temp[2]
        temp=''

if len(temp)%2==0:
        out[temp] = temp[0]+temp[-1]
        temp=''
else:
        out[temp] = temp[2]
        temp=''
print(out)