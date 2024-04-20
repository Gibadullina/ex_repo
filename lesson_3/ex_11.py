# Задание 11
print('ПН ВТ СР ЧТ ПТ СБ ВС')
st = []
week = ''
for x in range(0, 5):
    for z in range(1, 8):
        day = x*7+z
        if day // 10 == 0:
            week += ' ' + str(day) + ' '
        else:
            week += str(day) + ' '
        if day == 31:
            break
    print(week)
    week = ''
