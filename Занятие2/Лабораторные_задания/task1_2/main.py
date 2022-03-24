A = int(input('A:'))
B = int(input('B:'))

cond_1 = A % 2 == 1
cond_2 = B % 2 == 1

if cond_1 and cond_2:
    print('А и B нечетное число')
else:
    print('условия не прошли')