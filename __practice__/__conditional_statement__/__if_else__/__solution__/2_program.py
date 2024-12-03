#Write a program to check whether the given data is mutable or immutable

data = eval(input("Enter any form of value: "))

if type(data) in [list,set,dict]:
    print(data,"is a mutable data.")

else:
    print(data,"is a immutable data.")