#program_7. Write a program to print the sum of the first 10 Even numbers.

num= int(input("Enter the value to see the sum of the first 10 Even numbers: "))
count= 0    #to store counting
out= 0      #to store value of sum
i= 1 

while count<10: #for make sure sum of 10 even number
    
    print("Now value of i for condition is:",i ,end=" ---> ")
    
    if i%2==0:
        
        out+=i      #add the current even value of i to out
        
        count+=1    #increment count by 1

        print("Count after getting",i ,"as a even number : ",count,"\n")
    
    else:
        print(i,"is an odd number")
    
    i+=1            #increment i by 1

    

print("Sum of first 10 even number is: ",out)
    


