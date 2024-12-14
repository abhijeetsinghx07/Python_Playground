#Write a program to check whether the year is leap year or not.
'''
Explanation of Leap Year Rules
A year is a leap year if:

- It is divisible by 400, OR
- It is divisible by 4 but not divisible by 100.
'''

year = int(input("Enter the year to check: "))

if year%400==0 or (year%4==0 and year%100!=0) :
    print(f"{year} is leap year.")

else:
    print(f"{year} is not leap year.")