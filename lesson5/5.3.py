with open("text_3.txt", "r", encoding='utf-8') as f:
    my_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f"Зарплата = {round(sum(my_dict.values()) / len(my_dict), 3)}\n" f"Работники с зп меньше 20к {[e[0] for e in my_dict.items() if e[1] < 20000]}")