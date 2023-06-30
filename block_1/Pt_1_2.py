name = input('Введите имя: ').strip()
surname = input('Введите фамилию: ').strip()
result = " ".join([name, surname])
print(f'Полученная строка: {result}\nДлина строки: {len(result)}')
