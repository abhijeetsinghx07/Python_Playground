#program_6. Write a program to print the sum of the first 10 Natural numbers.


num= 10 #first 10 natural number
out= 0  #To store the value of sum
i= 1    #starting from 1 (natural number start from 1)

while i <= num:
    
    # print("Value of now i ",i)
    
    out+=i  #add the current value of i to out
    
    i+=1    #increment i by 1

    # print("Value of i after increment",i)

print("The sum of the first 10 natural numbers is: ",out)


