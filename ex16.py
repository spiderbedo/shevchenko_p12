text = input()
b = 0
for i in text:
    if i == '(':
        b += 1
    elif i == ')':
        b -= 1
print(b == 0)

