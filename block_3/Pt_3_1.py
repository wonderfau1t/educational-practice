from random import randint
# Генератор списка
lst = [randint(1, 10) for i in range(0, 10)]
# лямбда-функция для нахождения средненго значения списка
average = lambda lst: sum(lst) / len(lst)

print(lst)
print(average(lst))
