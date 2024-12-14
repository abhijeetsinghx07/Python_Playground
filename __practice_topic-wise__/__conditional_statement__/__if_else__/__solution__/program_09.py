#Write a program to check whether the given integer number is multiple of 10 or not.

num = int(input("Enter the value to check: "))

if num%10==0:
    print(f"Given integer {num} is multiple of 10. ")

else:
    print(f"Given integer {num} is not multiple of 10.")