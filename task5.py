my_list = [9, 8, 7, 6, 4, 5]
print(f"Рейтинг {my_list}")
num = int(input("Введите номер (0 является выходом из программы )"))
while num != 0:
    for i in range(len(my_list)):
        if my_list[i] == num:
            my_list.insert(i + 1, num)
            break
        elif my_list[-1] > num:
            my_list.append(num)
        elif my_list[0] < num:
            my_list.insert(0, num)
        elif my_list[i] > num and my_list[i + 1] < num:
            my_list.insert(i + 1, num)
    print(f"список {my_list}")
    num = int(input("Введите число "))
