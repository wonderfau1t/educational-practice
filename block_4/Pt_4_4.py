from itertools import combinations

target_number = int(input("Enter target bumber: "))
numbers = [1, 2, 3, 4, 5]

unique_combinations = []
suitable_combinations = []

for r in range(1, len(numbers) + 1):
    combinations_r = list(map(list, combinations(numbers, r)))
    unique_combinations.extend(combinations_r)

for combination in unique_combinations:
    if sum(combination) == target_number:
        suitable_combinations.append(combination)


print(f'Suitable combinations: {suitable_combinations}')