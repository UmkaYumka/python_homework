rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four:': 'Четыре'}
new_file = []
with open('task4.txt', 'r') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + ' ' + i[1])
    print(new_file)
with open('task4.txt', 't') as file_obj2:
    file_obj2.writelines(new_file)
