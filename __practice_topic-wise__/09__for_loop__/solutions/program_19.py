# 19. Write a program to toggle a string.

inp = input("Enter the string input: ")
out = ''

for i in inp:
    if 'A'<=i<='Z':
        out+=chr(ord(i)+32)

    elif 'a'<=i<='z':
        out+=chr(ord(i)-32)

    else:
        out+=i

print(out)