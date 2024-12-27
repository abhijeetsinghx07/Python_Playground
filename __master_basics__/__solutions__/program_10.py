#Write a program that accepts an integer (n) and computes the value of n+nn+nnn (expansion calculator).
'''
Sample value of n is 5

Expected Result : 615
'''

value = int(input("Enter value: "))

computes = value+(value*value)+(value*value*value)

print(f"Value after expansion of {value} is {computes}")
