# 14. Write a program to check whether the list is homogenous or not.

# [1,2,3,4,5]
# [1,2.0,0,'hey','',True,False,[3,4,5],[],(5,6,7),(),{55,44,55},{},{'a':100,'b':200},{}]

inp = [1,2,4,5,5]


checker=0

for i in range(1,len(inp)):
    if type(inp[0]) != type(inp[i]):
        checker+=1

if checker > 0:
    print("Given list is hetrogenous.")

else:
    print("Given list is homogenous.")
