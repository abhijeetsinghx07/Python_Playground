#Write a program that checks whether a specified value is contained within a group of values.
"""
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False"""

value= [1, 5, 8, 3]  #eval(input("Enter a list: "))
find=int(input("Enter value to find in list: "))


if find in value:
    print(f"Yes {find} is present in {value}") 

else:
    print(f"No {find} is not present in {value}") 