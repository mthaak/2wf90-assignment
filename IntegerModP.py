from common import *


class IntegerModP():
    """Integer mod prime p

    Attributes:
        i (int): number % p
        p (int): prime < 1000
    """

    def __init__(self, n, p):
        """Initialize an integer mod p.

        Args:
            n (int): number
            p (int): p < 1000

        :type n: int
        :type p: int
        """
        if type(n) != int:
            raise ValueError("Argument n is not an integer.")
        self.i = n % p

        if type(p) != int:
            raise ValueError("Argument p is not an integer.")
        if p > 1000:
            raise ValueError("Argument p is too large, should be smaller than 1000.")
        if not is_prime(p):
            raise ValueError("Argument p is not actually prime.")
        self.p = p

    # Decorator for all binary operations to check whether primes match
    def _check_p(func):
        def op(self, other):
            if self.p != other.p:
                raise ValueError("Primes are incompatible.")
            return func(self, other)

        return op

    # Decorator for power operations to check that power is a positive integer
    def _check_power(func):
        def operation(self, power):
            if type(power) != int:
                raise ValueError("Power is not an integer.")
            if power < 0:
                raise ValueError("Power is negative.")
            return func(self, power)

        return operation

    @_check_p
    def __add__(self, other):
        return IntegerModP(int.__add__(self.i, other.i) % self.p, self.p)

    @_check_p
    def __sub__(self, other):
        return IntegerModP(int.__sub__(self.i, other.i) % self.p, self.p)

    @_check_p
    def __mul__(self, other):
        return IntegerModP(int.__mul__(self.i, other.i) % self.p, self.p)

    @_check_p
    def __truediv__(self, other):
        return IntegerModP(int.__truediv__(self.i, other.i) % self.p, self.p)

    @_check_p
    def __floordiv__(self, other):
        return self.__truediv__(other)

    @_check_power
    def __pow__(self, power):
        return IntegerModP(int.__pow__(self.i, power) % self.p, self.p)

    @_check_p
    def __iadd__(self, other):
        self.i = int.__iadd__(self.i, other.i) % self.p

    @_check_p
    def __isub__(self, other):
        self.i = int.__isub__(self.i, other.i) % self.p

    @_check_p
    def __imul__(self, other):
        self.i = int.__imul__(self.i, other.i) % self.p

    @_check_p
    def __itruediv__(self, other):
        self.i = int.__itruediv__(self.i, other.i) % self.p

    @_check_p
    def __ifloordiv__(self, other):
        self.__itruediv__(other)

    @_check_power
    def __ipow__(self, power):
        self.i = int.__ipow__(self.i, power) % self.p

    def __str__(self):
        return str(self.i)

    def __repr__(self):
        return str(self.i) + " mod " + str(self.p)
