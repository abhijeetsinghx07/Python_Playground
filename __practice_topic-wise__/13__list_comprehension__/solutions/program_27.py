# 27. Extract all non-alphabetic characters from the string `"Py3th0n@2024!"`.

inp = "Py3th0n@2024!"

print([ i for i in inp if not('A'<=i<='Z' or 'a'<=i<='z')])