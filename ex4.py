a = input()
for i in a:
    b = 0
    for j in a:
        if j == i:
            b += 1
    if b == 3:
        print(i)
    break
