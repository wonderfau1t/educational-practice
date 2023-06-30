# Функция для геннерации случайных чисел
from random import randint

colors = {
    1: 'Зеленый',
    2: 'Желтый',
    3: 'Красный',
    4: 'Фиолетовый',
    5: 'Серый',
}

hints = {
    1: 'Движение разрешено!',
    2: 'Подожди следующий сигнал',
    3: 'Стой, движение запрещено',
    4: 'Этот цвет получается при смешивании синего и красного',
    5: 'Смешай белый и черный',
}


def print_colors() -> None:
    """Выводит список цветов"""
    print('Угадай цвет:')
    for key, value in colors.items():
        print(f'{key}. {value}')


def check_answer(programm_choice: int) -> bool:
    """
    Сравнивает выбор пользователя и программы
    :param programm_choice: "Правильный" ответ
    :return: Результат сравнения
    """
    user_choice = int(input('Введите цвет (указывать номер цвета): '))
    if programm_choice == user_choice:
        print('Отлично!')
        return True
    else:
        print(f'Подсказка: {hints[programm_choice]}')
        return False


def main():
    # Выбираем цвет, котоырй будет "правильным"
    programm_choice = randint(1, 5)
    print_colors()
    flag = False
    while not flag:
        flag = check_answer(programm_choice)


main()
