from common import *
from IntegerModP import IntegerModP
from PolynomialModP import PolynomialModP
from FiniteField import FiniteField


class SystemModP:
    """Arithmetic system mod prime p

    Attributes:
        p (int): prime < 100
    """

    def __init__(self, p):
        """Initialize a system mod p.

        Args:
            n (int): number
            p (int): p < 100

        :type p: int
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

    def int(self, n):
        """Create an integer mod p

        Args:
            n (int): number

        :type n: int
        """
        if type(n) != int:
            raise ValueError("Argument n is not an integer.")

        return IntegerModP(n, self.p)

    def poly(self):
        raise NotImplementedError

    def field(self):
        raise NotImplementedError
