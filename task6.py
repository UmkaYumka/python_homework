from itertools import count,cycle

my_count = count(3)
my_cycle = cycle("QWER")

for _ in range(5):
    print("(my_count,My_cycle) = ({},{})".format(next(my_count),next(my_cycle)))