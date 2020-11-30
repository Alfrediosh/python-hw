from functools import reduce


def my_list(el_p, el):
     return el_p * el


my_new_list = [el for el in range(99, 100) if el % 2 == 0]
print(f'list\n{my_new_list}\nMultiplication of numbers\n{reduce(my_list, my_new_list)}')