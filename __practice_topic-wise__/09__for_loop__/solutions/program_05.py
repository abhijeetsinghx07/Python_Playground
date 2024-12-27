# 5. Write a program to remove duplicates from list

value = [22,44,67,87,99,22,55,99] #eval(int(Enter a list: ))
out = []

for i in value:
    if i not in out:
        out.append(i)

print(out)