def is_prime(n):
    """Test if n is prime.

    Just some simple function to test primality for not too high numbers.

    Args:
        n (int) : Number to be tested
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


def prime_divisors(n):
    """Find prime factors of n.

     Returns divisors in a list.

    Args:
        n (int) : Number of which prime factors have to be found
    """
    divisors = [d for d in range(2, n // 2 + 1) if n % d == 0]
    return [d for d in divisors if all(d % od != 0 for od in divisors if od != d)] + [n]
