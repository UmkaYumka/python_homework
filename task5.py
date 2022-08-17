def summ():
    try:
        with open('task5,txt','w+') as file_obj :
            line = input("Введите числа через пробел\n")
            file_obj.writelines(line)
            my_num = line.split()

            print(sum(map(int,my_num)))
    except IOError:
        print("Произошла ошибка в файле")
    except ValueError:
        print("Ошибка во впемя ввода данных")
summ()