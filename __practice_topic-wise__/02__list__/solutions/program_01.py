# Write a Python program to sum all integers items in a list.

def sum(collection,sum=0):
    
    for i in collection:
        sum+=i

    return f"Sum of all number items in list are : {sum}"

print(sum(eval(input("Enter a list containing number as a item: "))))