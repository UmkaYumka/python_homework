def my_f():
    for w in input("Введите слова маленькими латинскими буквами,не забудьте про пробелы: \n").split():
        chars = 0
        for char in w:
            if 97 <= ord(char) <=122:
                chars += 1
        print(w.title() if chars == len(w) else f"{w} вводите только маленькие латинские буквы!")


my_f()
