a = input()

count = 1
maxc = 1

for i in range(len(a) - 1):
    if a[i] == a[i + 1]:
        count+=1
        if count > maxc:
            maxc = count
    else:
        count = 1
print(maxc)
