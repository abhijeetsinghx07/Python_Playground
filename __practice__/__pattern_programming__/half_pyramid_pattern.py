#Half pyramid pattern
'''
*
* *
* * *
* * * *
* * * * *
* * * * * *
'''

rows= int(input("Enter number of rows you want print in half pyramid pattern: "))

for i in range(rows):
    for j in range(i+1):
        print("*",end=' ')
    print()