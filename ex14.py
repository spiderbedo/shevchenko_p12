hint = input()
word = input()

for _ in range(25):
    print()

masked = []
for i in word:
    if i.isalpha():
        masked.append("*")
    else:
        masked.append(i)

attempts = 10

print(hint)

while attempts > 0:
    print("".join(masked))
    choice = input("Буква или слово (0 - буква, 1 - слово)? ")

    if choice == "0":
        letter = input("Буква: ")
        found = False
        for i, c in enumerate(word):
            if c == letter:
                masked[i] = word[i]
                found = True
        if not found:
            print("Такой буквы нет.")
            attempts -= 1
    
    else:
        guess = input("Слово: ")
        if guess == word:
            print("Победа!")
            exit()
        else:
            print("Неверное слово.")
            attempts -= 1

    if "*" not in masked:
        print("Победа!")
        exit()
        
print("Проигрыш!")
