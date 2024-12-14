#Write a program to take and consider a tuple collection consisting of only two values.
#Check whether the taken tuple is homogenous or heterogeneous.

value = eval(input("Enter two value for tuple: "))

if type(value[0]) == type(value[1]):
    print(f"The given tuple {value} is homogenous.")

else:
    print(f"The given tuple {value} is heterogeneous.")