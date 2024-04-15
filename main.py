print('Практическое задание ко 2 уроку')

# Пункт 1
str1 = input('Введите строку: ')
# print('Пункт 1')
# print('Строка в обратном порядке: 'str1[:: -1])

# Пункт 2
# print('Пункт 2')
str2 = str1[str1.find('h')+1:str1.rfind('h')]
str2 = str2.replace('h', 'H')

# print(str1[:str1.find('h')+1]+str2+str1[str1.rfind('h'):])


# Пункт 3
# print('Пункт 3')
print(f'Количество слов строке {str1}: ', len(str1.split()))


# Пункт 4
# print('Пункт 4')
print(f'Количество слов строке {str1}: ', str1.count(' ') + 1)

# Пункт 5
# print('Пункт 5')
str5 = 'практика задание'

list1 = str5.split()
str5 = f'{list1[1]} {list1[0]}'

print('Изменение порядка слов: ', str5)

# Пункт 6
# print('Пункт 6')
str3 = 'Иванова Снежана Алексеевна'
# str3 = input('Введите ФИО: ')

list6 = str3.split()
f_name = str(list6[1][0])
dd_name = str(list6[2][0])

print(list6[0]+' ' + f_name.upper()+'. '+dd_name.upper() + '.')

# Пункт 7
# print('Пункт 7')
list7 = [4, [4.0, [4+2j, ['', 4, 'Иголка']]]]

print(list7[1][1][1][2])

# Пункт 8
# print('Пункт 8')
list1 = [1, 2, 3]
list2 = [3, 4]

list8 = list1 + list2

# print(list3, ' Способ 1')

for x in list2:
    list1.append(x)
# print(list1, ' Способ 2')

# Пункт 9
# print('Пункт 9')
list1 = [4, 6, 8, 5, 3]
list2 = [1, 3, 4, 9]

list9 = list1 + list2

print(set(sorted(list9)))

# Пункт 10
# print('Пункт 10')
# неуникальные зн.
list10 = [1, 5, 6, 4, 6, 2, 7]
# уникальные зн.
# list10 = [1, 9, 2, 8, 3, 7, 4, 6, 5]

p10 = set(list10)

print(len(list10) == len(p10))

# Пункт 11
# print('Пункт 11')
date_dict = {'year': 2024, 'month': 4, 'day': 14}
# print(f'{date_dict['year']}-{date_dict['month']}-{date_dict['day']}')

# Пункт 12
# print('Пункт 12')
str12 = input('Введите числа через зяпутую: ')

el_str12 = str12.split(',')
int_list12 = map(int, el_str12)
tup = tuple(int_list12)

print('Список', el_str12, ' ', type(el_str12))
print('Кортеж: ', tup, ' ', type(tup))


# Пункт 13
# print('Пункт 13')
students = {'Schultz', 'Django', 'Brunhilde', 'Fritz'}
employees = {'Schultz', 'Django', 'Calvin', 'Butch', 'Fritz'}

print('Все люди: ', students | employees)
print('Все, кто учится и работает одновременно:', students & employees)
print('Все, кто только работает, но не учится:', employees - students)
print('Все, кто либо учится, либо работает, но не одновременно:', students ^ employees)

# Дополнительно

# Пункт 14
array = [
    [11, 12, 13, 14, 15],
    [21, 22, 23, 24, 25],
    [31, 32, 33, 34, 35],
    [41, 42, 43, 44, 45],
    [51, 52, 53, 54, 55]
]


# Пункт 15
