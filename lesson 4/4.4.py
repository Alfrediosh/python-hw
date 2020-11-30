from random import randint

my_list = [randint(-20, 20) for _ in range(10)]
my_new_list = [el for el in my_list if my_list.count(el) == 1]
print(f'Source list\n{my_list}\nNo repitition list\n{my_new_list}')
