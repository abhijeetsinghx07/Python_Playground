# 15. Create a list of all lowercase letters in the string `"HELLO Python"` without using the `.lower()` method.

inp = "HElLO Python"

print([i for i in inp if 'a'<=i<='z'])