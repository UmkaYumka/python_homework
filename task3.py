
class MyErr(Exception):
    def __init__(self):
        pass


class TypeCheck:
    def __init__(self):
        self.my_list = []

    def check_value(self):
        global user_val
        while True:
            try:
                try:
                    user_val = int(input('Введите числа: '))
                    ex = input(f'добавляем "{user_val}" в список. Хотите продолжить? y/n: ').lower()
                    self.my_list.append(user_val)
                    if ex == 'n':
                        print(self.my_list)
                        break
                except ValueError:
                    raise MyErr
            except MyErr:
                ex = input(f"Вы ввели не число. Хотите продолжить? y/n: ").lower()
                if ex == 'n':
                    print(self.my_list)
                    break
                else:
                    self.check_value()


a = TypeCheck()
a.check_value()