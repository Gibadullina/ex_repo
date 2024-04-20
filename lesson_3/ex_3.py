# Задание 3
fc = int(input('Введите число для расчета факториала: '))
solve = 1
for x in range(1, fc+1):
    solve *= x
    print(f'Шаг {x}: {x}! = {solve}')
print(f'Факториал числа {fc} равен: {solve}')