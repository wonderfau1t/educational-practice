string = input('Введите строку: ').strip()
# Разбиваем строку на слова по пробелам с помощью split()
# К каждому элементу массива с помощью функции map
# применяем функцию capitalize
result = list(map(str.capitalize, string.split()))

print(" ".join(result))
