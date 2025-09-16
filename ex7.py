sent = input().split()
minlen = 9999999
sw = ""
for i in sent:
    if len(i) < minlen:
        minlen = len(i)
        sw = i
print(sw)
