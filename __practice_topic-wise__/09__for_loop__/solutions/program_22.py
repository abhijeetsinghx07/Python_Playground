# 22. Write a program to get the following output.
 
"""
inp= ['[jiocinema.com](http://jiocinema.com/)', '[file.py](http://file.py/)', 'web.html', '[amazom.com](http://amazom.com/)', '[www.org](http://www.org/)"]
    
out= ['com', 'py', 'html','org"]

"""

inp   = ['jiocinema.com', 'file.py', 'web.html', 'amazom.com', 'www.org']

out = []

# temp=''

# # for i in inp:
# #     temp+=i
# #     out.append(temp[temp.index('.')+1:])
# #     temp=''

# # print(out)

for i in inp:

    out.append(i[i.index('.')+1:])

print(out)

