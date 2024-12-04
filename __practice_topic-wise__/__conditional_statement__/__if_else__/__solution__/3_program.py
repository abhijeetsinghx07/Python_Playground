#Write a program to check whether the given data is single value or collection.

data = eval(input("Enter the value to check: "))

if type(data) in [int,float,bool]:
    print(data,"is a single value.")

else:
    print(data,"is a collection.")