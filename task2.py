with open("tasl2.txt",  encoding="utf-8") as f:
    my_l = f.readlines()
    for ind,value in enumerate(my_l, 1):
        n_of_words = len(value.split())
        print(f"Строка {ind} содержит  {n_of_words} слов")
