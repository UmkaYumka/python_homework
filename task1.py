name = input("Введите ваше имя ")
year = int(input("Введите какой сейчас год "))
year_b = int(input("Введите ваш год рождения "))
age = year - year_b
country = input("в какой стране вы проживаете ")
city = input("в каком городе вы проживаете ")
inf = (f"вас зовут {name} , ваш год рождения {year_b} ,сейчас {year} год,ваш возраст {age}, ваша страна {country} ,ваш город {city}")
print(inf)
