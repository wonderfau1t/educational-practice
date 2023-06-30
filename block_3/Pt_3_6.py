# Use dict comprehension to create
# dictionary of numbers and their binary representation
bin_numbers = {n: bin(n)[2:] for n in range(1, 10 + 1)}

print(bin_numbers)