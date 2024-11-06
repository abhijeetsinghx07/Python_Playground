#Half pyramid pattern
rows= int(input("Enter number of rows you want print in half pyramid pattern: "))

for i in range(rows+1):
    for j in range(i):
        print("*",end=' ')
    print()

   