# Write a Python program to multiply all the items in a list.

def multiply(collection,result=1):
    
    for i in collection:
        result*=i

    return f"Result after multiply all items: {result}"

print(multiply(eval(input("Enter the list with containing number: "))))