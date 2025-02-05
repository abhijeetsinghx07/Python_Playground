# Write a Python program to get the largest number from a list.

def max(collection):
    
    temp = collection[0]

    for i in range(len(collection)):
        if collection[i] > temp:
            temp = collection[i]
        
    return temp   

print(max(eval(input("Enter a list containing some number: "))))