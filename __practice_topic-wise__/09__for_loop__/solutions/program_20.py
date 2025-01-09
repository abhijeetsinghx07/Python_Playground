# 20. Write a program extract upper, lower, digit and special characters present in a string.

inp = input("Enter the string value: ")
upper = []
lower = []
numeric = []
special = []

for i in inp:
    if 'A'<=i<='Z':
        upper.append(i)

    elif 'a'<=i<='z':
        lower.append(i)

    elif '0'<=i<='9':
        numeric.append(i)
    else:
        special.append(i)

print(f"Upper Case: {upper} \nLower Case: {lower} \nNumeric: {numeric} \nSpecial: {special}")

