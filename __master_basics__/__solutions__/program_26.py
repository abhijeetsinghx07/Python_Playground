#26. Write a program to create a histogram from a given list of integers.

"""
histogram([2, 3, 6, 5])

output:
        **                                                                                                            
        ***                                                                                                           
        ******                                                                                                        
        *****
"""

histogram=[2, 3, 6, 5, 8, 7, 9]

for i in histogram:
    print('*'*i,end='\n')


