def is_palindrome(substring: str) -> bool:
    """
    Check if a string is a palindrome
    :param substring: substring to check
    :return: True - if string is palindrome. Flase - if string isn't palindrome
    """
    return substring == substring[::-1]


def find_palindromes(string: str) -> list:
    """
    Finds all palindromes in a string
    :param string: string to check
    :return: list of palindromes
    """
    palindromes = []
    n = len(string)

    # Checking all substrings of string
    for i in range(n):
        for j in range(i + 1, n):
            substring = string[i:j]
            if is_palindrome(substring) and len(substring) > 1:
                palindromes.append(substring)

    return palindromes


input_string = input("Введите строку: ")
result = find_palindromes(input_string)
print("Палиндромы в строке:")
for palindrome in result:
    print(palindrome)
