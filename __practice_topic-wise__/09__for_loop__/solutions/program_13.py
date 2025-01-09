# 13. Write a program to extract all the non default values from a list.

inp = [1,2.0,0,'hey','',True,False,[3,4,5],[],(5,6,7),(),{55,44,55},{},{'a':100,'b':200},{}]

default_val= [0,0.0,'',False,[],(),{}]

out = []

for i in inp:
    if i not in default_val:
        out.append(i)

print(f"Non Default from given list are {out}")
