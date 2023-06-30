score = int(input('Введите полученое количество очков: '))
match score:
    case 3:
        print('Игра была выиграна')
    case 0:
        print('Игра была проиграна')
    case 1:
        print('Игра была сыграна вничью')
