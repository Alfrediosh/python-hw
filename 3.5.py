num = 0
try:
    while num != '#':
        for i in map(int, input("для входа наберите '#'\nВведите числа используя пробел\n").split()):
            num += i
        print(num)
except ValueError:
    print(num)