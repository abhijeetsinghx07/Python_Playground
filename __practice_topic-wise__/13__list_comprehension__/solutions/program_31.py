#31. Extract all uppercase letters from the string `"PyThoN ProGramMiNg"`.

word = "PyThoN ProGramMiNg"

uppercase = [i for i in word if 'A'<=i<='Z']

print(uppercase)