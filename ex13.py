count = 0
while True:
    ticket = input().strip()
    count += 1
    dig = [int(i) for i in ticket]
    a = len(dig)
    if a % 2 == 0:
        half = n // 2
        first = sum(dig[:half])
        sec = sum(dig[half:])
        if first == sec:
            print(count)
            break
