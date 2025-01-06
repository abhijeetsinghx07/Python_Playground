# 9. Write a program to extract all the key value pairs from the dictionary only if the keys are of string datatype and values are integers.

value = {'One':1, 'Two':2, 3:'Three', '4':4, 'Five':5, 'Six': '6'}
out = {}

for i in value:
    if type(i)==str and type(value[i])==int:
        out[i]=value[i]

print(out)