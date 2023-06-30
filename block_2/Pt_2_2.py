# Изначальный список програм
tv_program = ['Пусть говорят', 'Мужское/Женское', 'Что? Где? Когда?', 'Большие гонки']
# Печать списка програм
for i in range(0, len(tv_program)):
    print(f'{i+1}. {tv_program[i]}')

title = input('Введите название программы: ')
index = int(input('Выберите позицию, на которой она должна находится: '))

tv_program.insert(index - 1, title)

for i in range(0, len(tv_program)):
    print(f'{i+1}. {tv_program[i]}')
