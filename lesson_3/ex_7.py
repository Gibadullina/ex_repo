# Задание 7
str7 = input('Введите строку: ')


def check_palindrome(str1):
    for i in range(0, int(len(str1)/2)):
        if str1[i] != str1[len(str1)-i-1]:
            return False
    return True


check = check_palindrome(str7)
if check:
    print(f'Строка {str7} - палиндром')
else:
    print(f'Строка {str7} - не палиндром')


