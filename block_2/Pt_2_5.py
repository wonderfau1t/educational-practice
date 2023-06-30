from random import randint

count_of_games = 0
wins = 0
row = 0


def print_score():
    """Выводит информацию о сыгранных играх"""
    print('*' * 20)
    print(f'Игр: {count_of_games}\nПобед - {wins} | Проигрышы - {count_of_games - wins}\nОчередь из поражений - {row}')
    print('*' * 20)


while True:
    # Если пользователь проиграл 3 игры, то игра заканчивается
    if row == 3:
        print('Конец игры!')
        break
    # Правильный ответ
    right_answer = randint(0, 1)

    print('Выберите:\n0. Орел\n1. Решка')

    user_answer = int(input('Введите число: '))
    # Если пользователь ввел любое другое число
    if user_answer not in [0, 1]:
        print('Конец игры')
        break
    else:
        # Если пользователь отгадал, то ему засчитывается победа
        if user_answer == right_answer:
            print('-' * 10, 'Победа!', '-' * 10)
            wins += 1
            row = 0
        else:
            print('-' * 10, 'Проигрыш ;(', '-' * 10)
            row += 1
    count_of_games += 1
    print_score()
