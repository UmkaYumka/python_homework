my_list = []
el = int(input("Введите количество элементов списка "))
e = 0
i = 0
while i < el:
    my_list.append(input("Введите следующее значение списка "))
    i += 1
for e in range(int(len(my_list) / 2)):
    my_list[e], my_list[e + 1] = my_list[e + 1], my_list[e]
    e += 2
print(my_list)
