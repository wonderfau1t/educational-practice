def is_prime(n: int) -> bool:
    """
    Checks if a number is prime
    :param n: number to check
    :return: True – if prime, False - if not prime
    """
    if n < 2:
        return True
    else:
        for i in range(2, 10):
            if n % i == 0:
                return False
    return True


lst = [x for x in range(10) if not is_prime(x)]

print(lst)
