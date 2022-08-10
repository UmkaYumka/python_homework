def my_sum():
    sum = 0
    while True:
        f = False
        my_num = input("Введите любое число,для выхода введите E ").split()
        for num in my_num:
            if num.lower =='e':
                return sum

            else:
                try:
                    sum += int(num)
                except ValueError:
                    f = True
        if f:
            print("Данные некорректны")
        print(f"Сумма чисел = {sum}")


print(my_sum())
