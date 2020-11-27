def pers_info(name, surname, city, email):
    return f"Name - {name}; Surname - {surname}; City - {city}; Email - {email}"
print(pers_info(name=input("Введите своё имя "), surname=input("Введите свою фамилию "), city=input("Введите город рождения "), email=input("введите свой email ")))