# 26. Generate a list of even-indexed characters from `"Ichigo Kurosaki"`.

inp = "Ichigo Kurosaki"

print([inp[i] for i in range(len(inp)) if i % 2 == 0])

print()

print([(i,inp[i]) for i in range(len(inp)) if i % 2 == 0])