a = int(input('веедите число:'))

cond_1 = a % 2 == 0
cond_2 = a % 3 == 0

if cond_1 or cond_2:
    print("Число кратно 2 или 3")