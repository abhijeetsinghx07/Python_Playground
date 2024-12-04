#Write a program to check whether the first value present inside the given list is complex or not.


value = eval(input("Enter a list with five items: "))

if type(value[0]) == complex:
    print(f"First value in that list {value} is complex.")

else:
    print(f"First value in that list {value} is not complex.")