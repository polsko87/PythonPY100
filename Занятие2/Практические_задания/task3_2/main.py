A = 5
B = 7

cond_1 = A % 2 == 1
cond_2 = B % 2 == 1

if cond_1 and cond_2:  # ToDo напишите сюда условие проверки нечетности чисел А и B
    print('Числа А и B нечетные')
elif not cond_1 and not cond_2:
    print('Числа А  и B четные')
elif not cond_2:
    print('Числа B четные')
else:
    print('Числа А четные')