# Write a Python program to get the smallest number from a list.

def min(collection):
    temp = collection[0]
    for i in range(len(collection)):
        if collection[i]<temp:
            temp = collection[i]

    return temp 


print(min(eval(input("Enter the list that contain numbers: "))))