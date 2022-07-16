num = int(input("Введите любое число"))
m_num = num % 10
num = num // 10
while num > 0:
    if num % 10 > m_num:
        m_num = num % 10
    num = num // 10
print("Ваше самое большое число: ", m_num)
