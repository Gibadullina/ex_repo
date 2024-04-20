# Задание 5
n = int(input('Введите число n: '))
f = int(input('Введите число строк f: '))

print('\nТаблица умножения')

for x in range(1, f+1):
    print(f'{n} * {x} = {n*x}')