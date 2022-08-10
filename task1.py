def div(*args):
    try:
        num = int(input("Введите делимое число "))
        num2 = int(input("Введите делитель "))
        ans = num / num2
    except ValueError:
        return 'Err'
    except ZeroDivisionError:
        return "Делитель не может быть нулем, введите другое значение."
    return ans


print(f'Oтвет: {div()}')
