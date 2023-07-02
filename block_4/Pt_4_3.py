def is_prime(number: int) -> bool:
    """
    Checking if a number is prime
    :param number: number to check
    :return: True - if number is prime, False - if number isn't prime
    """
    for i in range(2, 9 + 1):
        if number % i == 0:
            return False
    return True


def find_prime_numbers(a: int, b: int) -> list:
    """
    Finds prime numbers in a given range
    :param a: Start of a range
    :param b: End of a range
    :return: list of prime sumbers
    """
    prime_numbers = []
    for n in range(a, b + 1):
        if is_prime(n):
            prime_numbers.append(n)
    return prime_numbers


a = int(input('Enter start of range: '))
b = int(input('Enter end of range: '))

print('Prime numbers: {}'.format(find_prime_numbers(a, b)))
