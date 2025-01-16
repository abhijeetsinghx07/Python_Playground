# 33. Generate a list of the last letters of words in `"Coding is fun with Python"`.

sentence = "Coding is fun with Python"

last_letters = [i[-1] for i in sentence.split()] 

print(last_letters)