my_list = [18, 2, 6, 1, 7, 5, 4, 13]
my_list_num = [my_list[num] for num in range(1, len(my_list)) if my_list[num > my_list[num - 1]]]
print(my_list_num)