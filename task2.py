my_list = [300, 2, 12, 44, 1, 2, 4, 10, 7, 1, 78, 123, 55]
my_newL = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f"Исходный список{my_list}")
print(f"Новый список{my_newL}")
