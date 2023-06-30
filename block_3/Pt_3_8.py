# Find out the ascii-code of the first letter of the alphabet
first_letter_index = ord('А')

alphabet = {chr(first_letter_index + i): i + 1 for i in range(0, 32)}

print(alphabet)