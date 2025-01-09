# 17. Write a program to get the following output.

"""  inp='always keep smiling'
     Out='syawla peek gnilims'
    
"""

inp = 'always keep smiling' #input("Enter the string value here: ")
out = ''
temp = ''

for i in inp:
    if i != ' ':
        temp = i+temp

    else:
        out+=temp+' '
        temp=''

out+=temp+' '
print(f"{inp} : {out}")