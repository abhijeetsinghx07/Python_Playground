# 25. Write a program to get the following output.
    
"""Inp='hello'
   
Out {0:'h', 1:'e', 2: 'l', 3:'l',4:'o'}"""

inp = input("Enter the value: ")
out = {}

for i in range(len(inp)):
    out[i]=inp[i]

print(out)


