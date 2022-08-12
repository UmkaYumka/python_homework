from functools import reduce


def my_fun(el_1, el_2):
    return el_1 * el_2


print(f"Четные значения{[el for el in range(99, 1001) if el & 2 == 0]}")
print(f"Перемножения всех элементов списка{reduce(my_fun, [el for el in range(99, 1001) if el & 2 == 0])}")
