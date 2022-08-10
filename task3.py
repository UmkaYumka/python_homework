def my_func(n1, n2, n3):
    try:
        my_l = list(map(float, [n1, n2, n3]))
        my_l.remove(min(my_l))
        return sum(my_l)
    except(ValueError):
        return "Можно ввести только числа."


print(my_func(input("Введите первое число"), input("Введите второе число"), input("Введите третье число")))
