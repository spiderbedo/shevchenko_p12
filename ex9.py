words = input().split()
b = set()
for i in words:
    if i in b:
        print(i)
        break
    else:
        b.add(i)
