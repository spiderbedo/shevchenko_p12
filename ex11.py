text = input().split()
cities = set()

for i in range(len(text)):
    city = text[i].lower()
    if city in cities:
        if i % 2 == 0:
            print("Вася")
        else:
            print("Петя")
        exit()
    if i > 0:
        p_last = text[i-1][-1].lower()
        c_first = text[i][0].lower()
        if p_last != c_first:
            if i % 2 == 0:
                print("Вася")
            else:
                print("Петя")
            exit()
    cities.add(city)
if n % 2 == 1:
    print("Петя")
else:
    print("Вася")
