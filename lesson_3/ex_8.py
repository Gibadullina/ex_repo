# Задание 8
str8 = input('Введите список через пробел: ')
list8 = str8.split(' ')


def check_duplicate(lst):
    for x in range(len(lst)):
        for z in range(x+1, len(lst)):
            if lst[x] == lst[z]:
                return False
    return True


check = check_duplicate(list8)
if check:
    print(f'Список не содержит дупликаты')
else:
    print(f'Список содержит дупликаты')
