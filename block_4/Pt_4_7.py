# Import a function from the itertools library to find permutations of a list
from itertools import permutations

lst = input('Enter list to find all permutations (to devide use comma): ').split(',')

permutations = permutations(lst)

for permutations in permutations:
    print(permutations)