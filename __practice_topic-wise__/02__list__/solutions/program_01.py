# Write a Python program to sum all the integers items in a list.

def sum(inp):
    
    total = 0
    for i in inp:
        total +=i
    
    return f'Sum of all the integer in list is: {total}'


print(sum(eval(input("Enter a list that contain int as elements: "))))