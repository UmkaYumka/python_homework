my_str = input("Введите строку ")
word = []
n = 1
for i in range(my_str.count(" ") + 1):
    word = my_str.split()
    if len(str(word)) <= 10:
        print(f"{n} {word[i]}")
        n += 1
    else:
        print(f"{n} {word [i] [0:10]}")
        n += 1
