def my_list(name, surname, year, city, email, phone):
    return ' '.join([name, surname, year, city, email, phone])


print(my_list(name=input("Введите ваше имя "), surname=input("Введите вашу фамилию"),
              year=input('Ввелите ваш год рождения'), city=input("Введите ваш город"),
              email=input("Введите вашу почту"), phone=input('Введите ваш номер телефона')))
