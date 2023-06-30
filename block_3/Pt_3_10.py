string = input('Input string: ')
# Counts of letters
letters = {letter: string.count(letter) for letter in string if letter != ' '}

print(letters)

