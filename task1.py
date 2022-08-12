from sys import argv


def zp():
    try:
        sal, time, prem = map(float, argv[1:])
        print(f" заработная плата сотрудника составляет: {time * sal + prem}")
    except ValueError:
        print("Данные введены неверно.")


zp()
