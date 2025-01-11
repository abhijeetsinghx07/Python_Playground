# 26. Write a program to extract all the string values present in list only if the string is palindrome.

inp = []
out = []

for i in range(1,6):
    x = input(f"Enter {i} string value: ")
    inp.append(x)

for j in inp:
    if j==j[::-1]:
        out.append(j)

print(f"These are palindrome string: {out}")
