# Write a Python program to count the number of strings from a given list of strings. 
# Those string length is 2 or more and also the first and last characters are the same.

# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : Count = 2 , strings = ['aba', '1221']

def count(user_input,result=[],count=0):
    for x in user_input:
        if len(x)>=2 and x[0]==x[-1]:
            count+=1
            result.append(x)

    return f"We have {count} string that are: {result}"

print(count(eval(input("Enter a list that contain string items: "))))