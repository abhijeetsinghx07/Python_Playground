# 15. Write a program to replace the space by present * in a string

inp = input("Enter the string: ")
out = ''

for i in range(0,len(inp)):
    if inp[i] != ' ':
        out+=inp[i]
    
    else:
        out+='*'
out+=inp[i]
print(out)