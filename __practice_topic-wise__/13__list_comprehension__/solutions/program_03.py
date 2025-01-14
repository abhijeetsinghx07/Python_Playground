# 3. Extract all vowels from the string `"Hello World"`.

inp = input("Enter a string: ")

print([i for i in inp if i in 'aeiouAEIOU'])