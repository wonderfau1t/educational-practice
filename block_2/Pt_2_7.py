summa = 0

while True:
    x = float(input('Введите отрицательное число: '))
    if x >= 0:
        print(f'Сумма введенных значений = {summa}')
        break
    else:
        summa += x
