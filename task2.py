sec = int(input("Введите время в секундах: "))
hour = sec // 3600
time = sec % 3600
min = time // 60
sec1 = time % 60
print(f"Время в секундах {hour}:{min}:{sec1}")
