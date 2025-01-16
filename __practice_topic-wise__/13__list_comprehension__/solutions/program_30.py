# 30. Create a list of numbers from 1 to 10 where even numbers are doubled, and odd numbers are halved.

number = [i**2 if i%2==0 else i/2 for i in range(1,11)]

print(number)