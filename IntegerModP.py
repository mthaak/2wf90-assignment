from common import *


class IntegerModP(int):
    """Integer mod prime p

    Attributes:
        i (int): number % p
        p (int): prime < 100
    """

    def __init__(self, n, p):
        """Initialize an integer mod p.

        Args:
            n (int): number
            p (int): prime < 100

        :type n: int
        :type p: int
        """
        if type(n) != int:
            raise ValueError("Argument n is not an integer.")
        self.n = n % p

        self.p = p

        super().__init__()

    def __new__(cls, n, p):
        return super().__new__(cls, n)

    # Decorator for all binary operations to check whether primes match
    def _check_p(func):
        def op(self, other):
            if self.p != other.p:
                raise ValueError("Primes are incompatible.")
            return func(self, other)

        return op

    @_check_p
    # Integer mod p addition
    def __add__(self, other):
        return IntegerModP(super().__add__(other.n) % self.p, self.p)

    @_check_p
    # Integer mod p subtraction
    def __sub__(self, other):
        return IntegerModP(super().__sub__(other.n) % self.p, self.p)

    @_check_p
    # Integer mod p multiplication
    def __mul__(self, other):
        return IntegerModP(super().__mul__(other.n) % self.p, self.p)

    @_check_p
    # Integer mod p division
    def __truediv__(self, other):
        return self.__floordiv__(other)

    @_check_p
    # Integer mod p division
    def __floordiv__(self, other):
        return IntegerModP(super().__floordiv__(other.n) % self.p, self.p)

    # Integer mod p exponentiation
    def __pow__(self, power):
        if type(power) != int:
            raise ValueError("Power is not an integer.")
        if power < 0:
            raise ValueError("Power is negative.")
        return IntegerModP(super().__pow__(power) % self.p, self.p)

    # @_check_p
    # def __iadd__(self, other):
    #     self.n = int.__add__(self.n, other.n) % self.p
    #     return self
    #
    # @_check_p
    # def __isub__(self, other):
    #     self.n = int.__sub__(self.n, other.n) % self.p
    #     return self
    #
    # @_check_p
    # def __imul__(self, other):
    #     self.n = int.__mul__(self.n, other.n) % self.p
    #     return self
    #
    # @_check_p
    # def __itruediv__(self, other):
    #     self.__ifloordiv__(other)
    #     return self
    #
    # @_check_p
    # def __ifloordiv__(self, other):
    #     self.n = int.__floordiv__(self.n, other.n) % self.p
    #     return self
    #
    # @_check_power
    # def __ipow__(self, power):
    #     self.n = int.__pow__(self.n, power) % self.p
    #     return self

    @_check_p
    # Integer mod p lower than
    def __lt__(self, other):
        return super().__lt__(other.n)

    @_check_p
    # Integer mod p lower than or equal to
    def __le__(self, other):
        return super().__le__(other.n)

    @_check_p
    # Integer mod p equal
    def __eq__(self, other):
        return super().__eq__(other.n)

    @_check_p
    # Integer mod p not equal
    def __ne__(self, other):
        return super().__ne__(other.n)

    @_check_p
    # Integer mod p greater than or equal to
    def __ge__(self, other):
        return super().__ge__(other.n)

    @_check_p
    # Integer mod p greater than
    def __gt__(self, other):
        return super().__gt__(other.n)

    def __int__(self):
        return self.n

    def __str__(self):
        return str(self.n) + " mod " + str(self.p)

    def __repr__(self):
        return str(self.n)
