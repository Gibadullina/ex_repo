print('Практическое задание ко 2 уроку')

# Пункт 1
str1 = input('Введите строку: ')
print('Пункт 1')
print('Строка в обратном порядке: ', str1[:: -1])

# Пункт 2
print('\nПункт 2')
str2 = str1[str1.find('h')+1:str1.rfind('h')]
str2 = str2.replace('h', 'H')

print(str1[:str1.find('h')+1]+str2+str1[str1.rfind('h'):])


# Пункт 3
print('\nПункт 3')
print(f'Количество слов строке {str1}: ', len(str1.split()))


# Пункт 4
print('\nПункт 4')
print(f'Количество слов строке {str1}: ', str1.count(' ') + 1)

# Пункт 5
print('\nПункт 5')
str5 = 'практика задание'

list1 = str5.split()
str5 = f'{list1[1]} {list1[0]}'

print(f'Изменение порядка слов в строке {str5} : ', str5)

# Пункт 6
print('\nПункт 6')
# str3 = 'Иванова Снежана Алексеевна'
str3 = input('Введите ФИО: ')

list6 = str3.split()
f_name = str(list6[1][0])
dd_name = str(list6[2][0])

print(list6[0]+' ' + f_name.upper()+'. '+dd_name.upper() + '.')

# Пункт 7
print('\nПункт 7')
list7 = [4, [4.0, [4+2j, ['', 4, 'Иголка']]]]

print(list7[1][1][1][2])

# Пункт 8
print('\nПункт 8')
list1 = [1, 2, 3]
list2 = [3, 4]

list8 = list1 + list2

print(list8, ' Способ 1')

for x in list2:
    list1.append(x)
print(list1, ' Способ 2')

# Пункт 9
print('\nПункт 9')
list1 = [4, 6, 8, 5, 3]
list2 = [1, 3, 4, 9]

list9 = list1 + list2

print(set(sorted(list9)))

# Пункт 10
print('\nПункт 10')
# неуникальные зн.
list10 = [1, 5, 6, 4, 6, 2, 7]
# уникальные зн.
# list10 = [1, 9, 2, 8, 3, 7, 4, 6, 5]

p10 = set(list10)

print(len(list10) == len(p10))

# Пункт 11
print('\nПункт 11')
date_dict = {'year': 2024, 'month': 4, 'day': 14}
print(f'{date_dict['year']}-{date_dict['month']}-{date_dict['day']}')

# Пункт 12
print('\nПункт 12')
str12 = input('Введите числа через зяпутую: ')

el_str12 = str12.split(',')
int_list12 = map(int, el_str12)
tup = tuple(int_list12)

print('Список', el_str12, ' ', type(el_str12))
print('Кортеж: ', tup, ' ', type(tup))


# Пункт 13
print('\nПункт 13')
students = {'Schultz', 'Django', 'Brunhilde', 'Fritz'}
employees = {'Schultz', 'Django', 'Calvin', 'Butch', 'Fritz'}

print('Все люди: ', students | employees)
print('Все люди: ', students.union(employees))
print('\nВсе, кто учится и работает одновременно:', students & employees)
print('Все, кто учится и работает одновременно:', students.intersection(employees))
print('\nВсе, кто только работает, но не учится:', employees - students)
print('Все, кто только работает, но не учится:', employees.difference(students))
print('\nВсе, кто либо учится, либо работает, но не одновременно:', students ^ employees)
print('Все, кто либо учится, либо работает, но не одновременно:', students.symmetric_difference(employees))

# Дополнительно

# Пункт 14
print('\nПункт 14')
array = [
    [11, 12, 13, 14, 15],
    [21, 22, 23, 24, 25],
    [31, 32, 33, 34, 35],
    [41, 42, 43, 44, 45],
    [51, 52, 53, 54, 55]
]

for i in range(len(array)):
    for j in range(len(array[i])):
        array[i][j] = array[j][i]
print(array)


# Пункт 15
print('\nПункт 15')
str15 = 5
# str15 = input ('Введите высоту пирамидки: ')
count = int(str15) * 2 + 2
text = 'x'
# text = input ('Введите символ для пирамидки: ')
for i in range(2, count, 2):
    txt = text*i
    txt1 = txt[:1].upper() + txt[1:]
    txt2 = txt1[:-1] + txt1[-1:].upper()
    print(txt2)
