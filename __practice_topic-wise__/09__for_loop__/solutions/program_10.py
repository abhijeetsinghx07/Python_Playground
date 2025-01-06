# 10. Write a program to extract key value pairs from the dictionary only if both keys and values are exactly same.

value = {'One':1, 'Two':2, 3:'Three', '4':4, 'Five':5, 'Six': '6'}
out   = {}
for i in value:
    if type(i) == type(value[i]):
        out[i]=value[i]

print(out)
