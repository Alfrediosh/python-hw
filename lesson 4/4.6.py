from itertools import count, cycle

my_count = count(int(input('Введите стартовое число ')), 5.8)
# my_cycle = cycle[True, 'ABC', 123, None] почему так не работает?
my_cycle = cycle("КАК")

for _ in range(10):
     print("(my_count, my_cycle) = ({},{})".format(next(my_count), next(my_cycle)))
