def is_prime(n):
    """Test if n is prime.

    Just some simple function to test primality for not too high numbers.

    Args:
        n (int) : Number to be tested

    :type n: int
    :return: bool
    """
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
