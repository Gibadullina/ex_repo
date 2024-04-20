
# Задание 2
array = ['Lisa', 'Aleksandra', 'Elis', 'Eva']
# 1 способ
print('Способ 1 цикл for')
max_len1 = ''
for name in array:
    if len(max_len1) < len(name):
        max_len1 = name
print('Самое длинное слово массива: ', max_len1)

# 2 способ
print('\nСпособ 2 цикл while')
max_len2 = ''
i = 0
while i < len(array):
    if len(max_len2) < len(array[i]):
        max_len2 = array[i]
    i += 1
print('Самое длинное слово массива: ', max_len2)
