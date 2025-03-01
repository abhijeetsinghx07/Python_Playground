# Write a Python program to multiply all the items in a list.

def multiply(inp):

    total = 1

    for i in inp:
        total *= i

    return total

print(multiply(eval(input("Enter a list contain numeric elements: "))))