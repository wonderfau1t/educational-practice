# String of vowels letters
vowels = 'уеёаоэяию'

string = input('Введите строку: ').lower()
# Value of every key depends on whether the letter is in the list of vowels
letters = {letter: True if letter in vowels else False for letter in string}

print(letters)
