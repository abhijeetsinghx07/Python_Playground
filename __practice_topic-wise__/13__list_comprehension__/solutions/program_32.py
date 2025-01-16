# 32. Create a list of all words in the sentence `"Practice makes perfect"` that start with `"p"`.

sentence = "Practice makes perfect"

word = [i for i in sentence.split() if any(i[j][0]=='P' or i[j][0]=='p' for j in range(len(i)))]

print(word)