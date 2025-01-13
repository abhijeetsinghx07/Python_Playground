#Write a program to get a newly-generated string from a given string where "Is" has been added to the front. 
#Return the string unchanged if the given string already begins with "Is".

value= input("Enter the string: ")

if value[0]=='I' and value[1]=='s':
    print(value)

else:
    value='Is'+value
    print(value)


