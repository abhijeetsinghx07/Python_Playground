# 23. Write a program to get the following output.
    
"""    
inp = ['jiocinema.com', 'file.py', 'web.html', 'amazom.com', 'www.org']

Out = {'com':['jiocinema', 'amazon'], 'py': ['file', 'python'], 'html':["web"], 'or':["www"]}

"""

inp = ['jiocinema.com', 'file.py', 'web.html', 'amazom.com', 'www.org']
out = {}
temp_l = []

for i in inp:
    temp=i[i.index('.')+1:]

    if temp in inp:
        temp_l.append(i)    
        temp=''

print(temp)
print(temp_l)
print(out)

