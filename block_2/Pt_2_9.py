n = input('Введите натуральное число, цифры которого различны: ')
# Преобразуем строку в массив целых значений
list_of_digit = list(map(int, n))
# Ищем максимальую цифру
max_ = max(list_of_digit)
# Узнаем индекс максимальной цифры
index_of_max = list_of_digit.index(max_)

print(f'''Порядковый номер максимальной цифры:
Считая номера от начала = {index_of_max + 1}
Считая от конца = {len(list_of_digit) - index_of_max}''')


