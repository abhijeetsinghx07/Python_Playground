# 7. Create a list of the lengths of words in the sentence `"Python list comprehensions are powerful."`.

sentence = "Python list comprehensions are powerful."
out=0

print([ len(i)  for i in sentence.split(' ')])