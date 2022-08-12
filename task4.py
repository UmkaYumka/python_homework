my_list = [2, 1, 4, 5, 5, 6, 6, 7, 8, 9, 8, 10]
my_newL = [el for el in my_list if my_list.count(el) == 1]
print(my_newL)
