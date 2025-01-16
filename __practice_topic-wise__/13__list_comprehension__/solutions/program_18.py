# 18. Create a list of words in the sentence `"List comprehension in Python"` that have more than 4 characters.

sentence = "List comprehension in Python"

print([i for i in sentence.split() if len(i)>4])