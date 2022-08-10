def my_pow(x,y):
    try:
        ans = x**y
    except TypeError:
        return "Введите десятичную дробь и отрицательную степень"
    return ans


print(my_pow(5.5,-3))
