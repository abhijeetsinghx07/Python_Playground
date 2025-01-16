# 19. Extract all numbers divisible by both 2 and 3 from the list `[6, 12, 15, 22, 18, 30]`.

num = [6, 12, 15, 22, 18, 30]

print([i for i in num if i%2 == 0 and i%3 == 0])