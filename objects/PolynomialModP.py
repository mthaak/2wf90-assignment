from common import *
from objects.IntegerModP import IntegerModP


class PolynomialModP():
    """Polynomial mod prime p

    Attributes:
        coefs (int): numbers % p, denoting coefficients of polynomial from most to least significant
        p (int): prime < 100
    """

    def __init__(self, coefficients, p):
        """Initialize a polynomial mod p.

        Args:
            n (int): number
            p (int): prime < 100
        """
        if type(p) != int:
            raise ValueError("Argument p is not an integer.")
        if p < 2:
            raise ValueError("Argument p is too small, should be larger than 1.")
        if p > 100:
            raise ValueError("Argument p is too large, should be smaller than 100.")
        if not is_prime(p):
            raise ValueError("Argument p is not actually prime.")
        self.p = p

        for i in range(1, len(coefficients)):
            if type(coefficients[i]) != int:
                raise ValueError("Argument " + coefficients[i] + " + is not an integer.")

        # TODO Implement
        # TODO Clean comments/docstring

        self.coefs = []
        for c in coefficients:
            self.coefs.append(IntegerModP(c, p))

    # Decorator for all binary operations to check whether primes match
    def _check_p(func):
        def op(self, other):
            if self.p != other.p:
                raise ValueError("Primes are incompatible.")
            return func(self, other)

        return op

    def terms(self):
        return self.coefs.size()

    # function value of x
    def f(self, x):
        raise NotImplementedError

    @_check_p
    # polynomial gcd
    def gcd(self, other):
        raise NotImplementedError

    # test congruence with some other polynomial modulo mod
    def congruent(self, other, mod):
        raise NotImplementedError

    @_check_p
    # sum
    def __add__(self, other):
        raise NotImplementedError

    @_check_p
    # difference
    def __sub__(self, other):
        raise NotImplementedError

    @_check_p
    # scalarmultiple & product
    def __mul__(self, other):
        raise NotImplementedError

    @_check_p
    # longdivide
    # returns quotient and remainder
    def __truediv__(self, other):
        raise NotImplementedError

    @_check_p
    # equal
    def __eq__(self, other):
        raise NotImplementedError

    @_check_p
    # not equal
    def __ne__(self, other):
        raise NotImplementedError
