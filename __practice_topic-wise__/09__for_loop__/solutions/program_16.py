#16. Write a program to count the number of occurrence of a specified character.

inp = input("Enter tha value to check occurrence: ")
char = input("Enter specific character you want to check: ")
count = 0

for i in inp:
    if i == char:
        count+=1

print(f"Character '{char}' have occured {count} times in {inp}")


