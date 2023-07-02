number = input('Input number: ')
# Сonvert the string to an array of integers
digits = list(map(int, number))
# Sort by decreasing
digits.sort(reverse=True)
# Convert array of integers to an array of strings
str_digits = list(map(str, digits))
# Concatenate the elements of a list into one string
print(f'Max number of these digits', ''.join(str_digits))
