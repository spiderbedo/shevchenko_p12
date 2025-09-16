words = input().split()
fw = words[0]
result = []
for i in words:
    if i != fw and len(i) == len(set(i)):
        result.append(i)
print(result)

