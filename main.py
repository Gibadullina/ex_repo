print('Практическое задание ко 2 уроку')

#Пункт 1
str1 = input('Введите строку: ')
#print('Пункт 1')
#print('Строка в обратном порядке: 'str1[:: -1])

#Пункт 2
#print('Пункт 2')
str2=str1[str1.find('h')+1:str1.rfind('h')]
str2=str2.replace('h','H')
#print(str1[:str1.find('h')+1]+str2+str1[str1.rfind('h'):])


#Пункт 3
#print('Пункт 3')
print(len(str1.split()))


#Пункт 4
#print('Пункт 4')
print(str1.count(' ') + 1)

#Пункт 5
#print('Пункт 5')
str2 = 'практика задание'
list1 = str2.split()
str2 = f'{list1[1]} {list1[0]}'
print(str2)

#Пункт 6
#print('Пункт 6')
str3 = 'Иванова Снежана Алексеевна'
#str3 = input('Введите ФИО: ')
list = str3.split()
f_name = str(list[1][0])
dd_name = str(list[2][0])
print(list[0]+' '+ f_name.upper()+'. '+dd_name.upper() +'.')

#Пункт 7
#print('Пункт 7')
list3 = [4, [4.0, [4+2j, ['', 4, 'Иголка']]]]
print(list3[1][1][1][2])

#Пункт 8
#print('Пункт 8')
list1 = [1, 2, 3]
list2 = [3, 4]
list3 = list1 + list2
#print(list3, ' Способ 1')

for x in list2:
    list1.append(x)
#print(list1, ' Способ 2')

#Пункт 9
#print('Пункт 9')

#Пункт 10
#print('Пункт 10')

#Пункт 11
#print('Пункт 11')
date_dict = {'year': 2024, 'month': 4, 'day': 14}
#print(f'{date_dict['year']}-{date_dict['month']}-{date_dict['day']}')

#Пункт 12
#print('Пункт 12')

#Пункт 13
#print('Пункт 13')

#Дополнительно
#Пункт 14

#Пункт 15







