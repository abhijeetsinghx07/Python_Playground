# 24. Write a program to get the following output.
    

"""
inp = ['hai',34,3.4,'hello',90,'byebye']
    
Out = {'hai': 'hi', 'hello': 'ho', 'byebye":"be"}
"""

inp = ['hai',34,3.4,'hello',90,'byebye']
out = {}

for i in inp:
    if type(i)==str:
        
        out[i]=i[0]+i[-1]
    

print(out)





