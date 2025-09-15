a = input()
count = 0
maxs = 0

for i in a:
    if i == " ":
        count+=1
        if count > maxs:
            maxs = count
    else:
        count = 0
print(maxs)
