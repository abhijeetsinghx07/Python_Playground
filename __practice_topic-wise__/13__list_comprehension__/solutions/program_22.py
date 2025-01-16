# 22. Extract all numbers that are prime from the range 1 to 20.

# print([ [(i,'Not-Prime') if i%j==0 else (i,'Prime') for j in range(2,i)] for i in range(1,21)])

# for i in range(1,9):
#     for j in range(2,i):
#         print(f"i:{i} j:{j}")
#         if i%j!=0:
#             print(f"{i} Prime")
#         # else:
#         #     print(f"{i} Prime")

print([num for num in range(2,22) if all(num % i != 0  for i in range(2,num))])

# for i in range(2,22):
#     for j in range(2,i):
#         if all(i % j != 0):
#             print(i)