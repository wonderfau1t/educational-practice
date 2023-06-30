def is_armstrong_number(number: int) -> bool:
    """
    Проверяетя является ли число нарциссическим
    :param number: Число для проверки
    """
    summa = 0
    # Проходимся по каждой цифре из числа
    for digit in str(number):
        # Завершаем цикл, если сумма уже превысила предел
        if summa > number:
            return False
        else:
            # Возводим каждую цифру в степень равной количеству цифр в числе
            summa += int(digit) ** len(str(number))
    if summa == number:
        return True
    else:
        return False


x = int(input('Введите число: '))

if is_armstrong_number(x):
    print(f'{x} явялется числом Армстрогна')
else:
    print(f'{x} не является числом Армстронга')