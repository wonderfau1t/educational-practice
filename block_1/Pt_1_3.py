# Запрос чисел у пользователя
numbers = [int(input('Введите число: ')) for i in range(0, 3)]

print(f'Максимальное число: {max(numbers)}\nОтсортированный список: {sorted(numbers)}')
