# Задание 4
# 1 способ (без ввода данных)
list2 = ['Rose', 'Tulip', 'Iris', 'Blueberry', 'Strawberry', 'Raspberry']
for i, j in enumerate(list2, start=1):
    if i % 3 == 0:
        print(i, j)

# 2 способ (ввод данных)
print('\nСпособ 2')
n = int(input('Введите длину списка: '))
list1 = []
for x in range(n):
    list1.append(input('Введите элемент списка: '))
for i, j in enumerate(list1, start=1):
    if i % 3 == 0:
        print(i, j)
