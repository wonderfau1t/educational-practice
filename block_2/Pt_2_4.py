# Функция для извелечения квадратного корня из числа
from math import sqrt
# Какое количество знаков после запятой
decimal = 3


def solve_equation(a, b, c) -> None:
    """
    Решает квадратное уравнение
    :param a: коэффициент a
    :param b: коэффициент b
    :param c: коэффициент c
    :return: выводит корни уравнения
    """
    d = b ** 2 - 4 * a * c

    if d == 0:
        x = round((-b / (2 * a)), decimal)
        print(f'Корень уравнения:\nx = {x}')
    elif d > 0:
        x1 = round((-b + sqrt(d)) / (2 * a), decimal)
        x2 = round((-b - sqrt(d)) / (2 * a), decimal)
        print(f'Корни уравнения:\nx1 = {x1}\nx2 = {x2}')
    else:
        print('Корней нет!')


a = int(input('Введите коэффициент a: '))
b = int(input('Введите коэффициент b: '))
c = int(input('Введите коэффициент c: '))

solve_equation(a, b, c)

