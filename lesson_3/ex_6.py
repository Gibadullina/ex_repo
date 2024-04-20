# Задание 6

# 1 способ
print('Способ 1 цикл for')

number1 = int(input('Введите число: '))
count1 = 0

for x in str(number1):
    count1 += 1
print(f'Количество цифр в числе = {count1}')

# 2 способ
print('\nСпособ 2 цикл while')

number2 = int(input('Введите число: '))
count2 = 0

while number2 > 0:
    count2 += 1
    number2 //= 10
print(f'Количество цифр в числе = {count2}')
