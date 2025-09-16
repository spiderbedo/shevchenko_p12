numb = input()
for i in range(25): 
    print()
for j in range(10):
    attempt = input()
    bull = sum(1 for k in range(4) if attempt[k] == numb[k])
    cow = sum(1 for n in attempt if n in numb) - bull
    print("Быков:", bull, "Коров:", cow)
    if bull == 4:
        print("Победа!")
        break
else:
    print("Проигрыш!")
