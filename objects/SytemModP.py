from common import *
from objects.IntegerModP import IntegerModP
from objects.PolynomialModP import PolynomialModP


# TODO test derivation int
# TODO implement and test other derivations

class SystemModP:
    """Arithmetic system mod prime p

    Attributes:
        p (int): prime < 100
    """

    def __init__(self, p):
        """Initialize a system mod p.

        Args:
            p (int): prime < 100
        """
        if type(p) is not int:
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
        Returns:
            IntegerModP(n, self.p)
        """
        return IntegerModP(n, self.p)

    def poly(self, coefficients):
        """Create a polynomial mod p

        Args:
            coefficients (int): coefficients sorted from most to least significant
        Returns:
            PolynomialModP(coefficients, self.p)
        """
        return PolynomialModP(coefficients, self.p)

    def field(self, ):
        """Create a finite field mod p with some irreducible polynomial f

        Args:
        """""
        raise NotImplementedError
