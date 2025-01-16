# 29. Generate a list of palindromic numbers from 1 to 100.

plaindromic_num = [i for i in range(1,1001) if str(i) == str(i)[::-1]]

print(plaindromic_num)