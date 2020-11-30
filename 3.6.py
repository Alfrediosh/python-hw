def int_func(word):
    for word in input("Введите слова через пробел(латиницей в нижнем регистре):\n").split():
        chars = 0
        for char word:
            if 97 <= ord(char) <= 122:
                chars += 1
        print(word.title() if chars == len(word) else f"{word} - только английские буквыБ маленькие!")
    int_func()