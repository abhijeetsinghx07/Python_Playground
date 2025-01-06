#27. Write a program that concatenates all elements into a string and returns it.

value = [1,2,"hello",55,"hey"]
result=''

for i in value:
    result+=str(i)

print(result)

