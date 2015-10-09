from common import *


class IntegerModP(int):
    """Integer mod prime p

    Attributes:
        n (int): number % p
        p (int): prime
    """

    def __init__(self, n, p):
        """Initialize an integer mod p.

        Args:
            n (int): number
            p (int): prime < 100
        """
        if type(n) is not int:
            raise ValueError("Argument n is not an integer.")
        self.n = n % p

        if type(p) is not int:
            raise ValueError("Argument p is not an integer.")
        if p < 2:
            raise ValueError("Argument p is too small, should be larger than 1.")
        if p > 100:
            raise ValueError("Argument p is too large, should be smaller than 100.")
        if not is_prime(p):
            raise ValueError("Argument p is not actually prime.")
        self.p = p

        super().__init__()

    def __new__(cls, n, p):
        return super().__new__(cls, int(n) % p)

    # Decorator for all binary operations to check whether primes match
    def _check_p(func):
        def op(self, other):
            if type(other) is IntegerModP:
                if self.p != other.p:
                    raise ValueError("Primes are incompatible.")
            elif type(other) is not int:
                raise ValueError("Operand type " + type(other) + "is not supported.")
            return func(self, other)

        return op

    @_check_p
    # Integer mod p addition
    def __add__(self, other):
        """Add other IntegerModP or int."""
        return IntegerModP(super().__add__(other) % self.p, self.p)

    @_check_p
    # Integer mod p subtraction
    def __sub__(self, other):
        """Subtract other IntegerModP or int."""
        return IntegerModP(super().__sub__(other) % self.p, self.p)

    @_check_p
    # Integer mod p multiplication
    def __mul__(self, other):
        """Multiply with other IntegerModP or int."""
        return IntegerModP(super().__mul__(other) % self.p, self.p)

    @_check_p
    # Integer mod p division
    def __truediv__(self, other):
        """Divide by other IntegerModP or int, such that self = other * result (mod p)."""
        if type(other) is int: other = IntegerModP(other, self.p)
        return IntegerModP(next(i for i in range(self.p) if other * i == self), self.p)

    @_check_p
    # Integer mod p division
    def __floordiv__(self, other):
        """Divide by other IntegerModP or int, returns only the quotient."""
        return IntegerModP(super().__floordiv__(other) % self.p, self.p)

    @_check_p
    # Integer mod p modulo
    def __mod__(self, other):
        """Modulo by other IntegerModP or int."""
        return IntegerModP(int(super().__mod__(other)), int(other))

    @_check_p
    # Integer mod p exponentiation
    def __pow__(self, other):
        """Raise to the power."""
        if other < 0:
            raise ValueError("Power is negative.")
        return IntegerModP(super().__pow__(other) % self.p, self.p)

    # Integer mod p negation
    def __neg__(self):
        """Negate."""
        return IntegerModP(super().__neg__() % self.p, self.p)

    def __str__(self):
        return "{0} (mod {1})".format(str(self.n), str(self.p))

    def __repr__(self):
        return "IntegerModP({0}, {1})".format(str(self.n), str(self.p))
