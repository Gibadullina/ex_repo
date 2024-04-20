# Задание 9
# 1 способ
str9 = input('Введите список через пробел: ')
list9 = str9.split(' ')
lst = sorted(list9)
lst_new = [lst[0]]
for x in range(1, len(lst)):
    if lst[x] == lst[x-1]:
        print('Дупликат: ', lst[x])
    else:
        lst_new.append(lst[x])
print(lst_new)


# 2 способ
print('Способ 2')
i = 1
j = 0
lst1 = sorted(list9)
lst_new1 = [lst1[0]]
while i < len(list9):
    if list9[i-1] != list9[i]:
        lst_new1.append(lst1[i])
    i += 1
print(lst_new1)
