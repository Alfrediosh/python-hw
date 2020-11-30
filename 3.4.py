def my_func(a, b):
    try:
        a, b = float(a), int(b)
        if a <= 0 or b >= 0:
            return "Не выполненно условие: \na должно быть больше 0\nb должно быть меньше 0"
        else:
            result = 1
            for _ in range(abs(b)):
                result /=a
            return f'Результат возведения а в степень b: {round(result, 6)}'
    except ValueError:
        return "Только числа"
    num_1 = input("Введите действительное положительное число, а = ")
    num_2 = input("Введите целое отрицательное число, b = ")
    print(my_func(num_1, num_2))