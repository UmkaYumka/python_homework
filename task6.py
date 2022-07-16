a = float(input("Введите вашу ежедневную норму во время пробежки в км "))
b = float(input("Введите вашу конечную цель в км"))
d = 1
if a > b:
    print(d)
while True:
    if a <= 0 or b <= 0:
        print("для начала вам стоит начать бегать")
    else:
        while a < b:
            a = a + a / 10
            d += 1
        print(f"вы достигните свою цель в {b} км на {d}-й день")
        break
