def div(num_1, num_2):
    try:
        num_1, num_2 = int(num_1), int(num_2)
        div_num = num_1 / num_2
    except ValueError:
        return "Ошибонька"
    except ZeroDivisionError:
        return "значение ниже нуля запрещено"
    return round(div_num, 4)
print(div(input("Введите первое число "), input("Введите второе число ")))