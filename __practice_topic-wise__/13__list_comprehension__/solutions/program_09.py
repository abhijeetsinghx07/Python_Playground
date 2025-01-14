# 9. Generate a list of characters in the string `"Python"` excluding vowels.

word = "Python"

print([i for i in word if i not in 'aeiouAEIOU'])