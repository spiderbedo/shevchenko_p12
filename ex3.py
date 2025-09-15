a = input()

lt = set()
for i in a.lower():
    if i.isalpha():
        lt.add(i)

print(len(lt))
