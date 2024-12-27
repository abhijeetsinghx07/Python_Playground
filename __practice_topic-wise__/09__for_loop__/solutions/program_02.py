# 2. Write a program to print all the integers present in a list.

value= [22,33,'Roses',55,'are',87,'Red'] #eval(input("Enter a hetrogenous list:"))

for i in value:
    if type(i) == int:
        print(i)
