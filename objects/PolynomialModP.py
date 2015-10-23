from common import *
from objects.IntegerModP import IntegerModP
import itertools


class PolynomialModP(list):
    """Polynomial mod prime p

    Attributes:
        coefs (list): list of IntegerModP, sorted from most to least significant
        p (int): prime
    """

    def __init__(self, coefficients, p):
        """Initialize a polynomial mod p.

        Args:
            coefficients (list): list of IntegerModP or int, sorted from most to least significant
            p (int): prime < 100
        """
        if type(coefficients) is not list:
            raise ValueError("Argument coefficients is not a list.")
        coefs = []
        skip_zeros = True  # The first * number of zero coefficients should not be included
        for i, c in enumerate(coefficients):
            if c % p != 0 or not skip_zeros or i == len(coefficients) - 1:
                # all coefficients are forced modulo of p
                if type(c) is IntegerModP:
                    coefs += [IntegerModP(c.n % p, p)]
                elif type(c) is int:
                    coefs += [IntegerModP(c, p)]  # int is converted to IntegerModP
                else:
                    raise ValueError("Coefficient " + str(c) + " is not an IntegerModP or int.")
            if c % p != 0 and skip_zeros:
                skip_zeros = False
        self.coefs = coefs

        if type(p) is not int:
            raise ValueError("Argument p is not an integer.")
        if p < 2:
            raise ValueError("Argument p is too small, should be larger than 1.")
        if p > 100:
            raise ValueError("Argument p is too large, should be smaller than 100.")
        if not is_prime(p):
            raise ValueError("Argument p is not actually prime.")
        self.p = p

        super().__init__(self.coefs)

    # Decorator for all binary operations to check whether primes match
    # Also converts other to PolynomialModP if needed
    def _check_p(func):
        def op(self, other, *args):
            if type(other) is PolynomialModP:
                if self.p != other.p:
                    raise ValueError("Primes are incompatible.")
            elif type(other) is IntegerModP:  # operation with IntegerModP allowed
                if self.p != other.p:
                    raise ValueError("Primes are incompatible.")
                other = PolynomialModP([int(other)], self.p)
            elif type(other) is int:  # operation with int allowed
                other = PolynomialModP([other], self.p)
            elif type(other) is list:  # operation with list allowed
                other = PolynomialModP(other, self.p)
            else:
                raise ValueError("Operand type " + str(type(other)) + "is not supported.")
            return func(self, other, *args)

        return op

    # Clone self to prevent mutation
    def clone(self):
        """Clone self."""
        return PolynomialModP(self.coefs, self.p)

    def degree(self):
        """Get the degree."""
        return len(self.coefs) - 1

    # Function value of x
    def f(self, x):
        """Calculate the image of x."""
        result = 0
        t = 1  # term
        for c in reversed(self.coefs):
            result += c.n * t
            t *= x
        return result

    # Long division
    def long_divide(self, other):
        """Long divide by other PolynomialModP, returns (quotient, remainder) as tuple."""
        # Based on algorithm 1.2.6
        q = PolynomialModP([0], self.p)  # quotient
        r = self.clone()  # remainder
        d = other  # divisor
        while r.degree() > d.degree() or (r.degree() == d.degree() and r.coefs[-1] >= d.coefs[-1]):
            f_coefs = [int(r.coefs[0] / d.coefs[0])]  # coefficient of term
            f_coefs += (r.degree() - d.degree()) * [0]  # Pad with zero's to denote order
            f = PolynomialModP(f_coefs, self.p)  # factor
            r -= f * d
            q = q + f
        return q.clone(), r.clone()

    @_check_p
    # Polynomial mod p gcd using Euclidean algorithm
    def gcd(self, other):
        """Calculate the gcd with other PolynomialModP, returns (gcd, x, y) as tuple s.t. gcd = x * self + y * other."""
        # Based on algorithm 1.2.11
        a = self.clone()
        b = other.clone()
        x, y, u, v = 0, 1, 1, 0
        while a != 0:
            q, r = b.long_divide(a)
            m, n = x - u * q, y - v * q
            b, a, x, y, u, v = a, r, u, v, m, n
        return b.clone(), x.clone(), y.clone()

    @_check_p
    # Polynomial mod p congruence with other polynomial modulo k
    def congruent(self, other, k):
        """Test congruence with other PolynomialModP (mod k)"""
        return (self - other) % k == 0

    @_check_p
    # Polynomial mod p addition (sum)
    def __add__(self, other):
        """Add other PolynomialModP."""
        d, e = [0] * (len(other) - len(self)), [0] * (len(self) - len(other))  # Padding to make lists equal length
        coefs = [(i + j) % self.p for i, j in zip(d + self.coefs, e + other.coefs)]
        return PolynomialModP(coefs, self.p)

    # Makes add operation commutative, so result is in both cases a PolynomialModP
    @_check_p
    def __radd__(self, other):
        return other.__add__(self)

    @_check_p
    # Polynomial mod p subtraction (difference)
    def __sub__(self, other):
        """Subtract other PolynomialModP."""
        d, e = [0] * (len(other) - len(self)), [0] * (len(self) - len(other))  # Padding to make lists equal length
        coefs = [(i - j) % self.p for i, j in zip(d + self.coefs, e + other.coefs)]
        return PolynomialModP(coefs, self.p)

    # Makes subtract operation commutative
    @_check_p
    def __rsub__(self, other):
        return other.__sub__(self)

    @_check_p
    # Polynomial mod p multiplication (scalar multiple & product)
    def __mul__(self, other):
        """Multiply with other PolynomialModP (or IntegerModP/int for scalar multiple)."""
        coefs = (self.degree() + other.degree() + 1) * [0]
        for i in range(0, len(self)):
            for j in range(0, len(other)):
                coefs[i + j] += self.coefs[i] * other.coefs[j]
        return PolynomialModP(coefs, self.p)

    # Makes multiply operation commutative
    @_check_p
    def __rmul__(self, other):
        return other.__mul__(self)

    @_check_p
    # Division operation makes use of long division
    def __truediv__(self, other):
        """Divide by other PolynomialModP."""
        return self.long_divide(other)[0]

    @_check_p
    # Modulo operation makes use of long division
    def __mod__(self, other):
        """Modulo by other PolynomialModP."""
        return self.long_divide(other)[1]

    # Power operation
    def __pow__(self, power):
        """Raise to the power of other PolynomialModP."""
        if power == 0:
            return PolynomialModP([1], self.p)
        else:
            return self * self.__pow__(power - 1)

    @_check_p
    # Polynomial mod p equal
    def __eq__(self, other):
        """Test if equal to other PolynomialModP."""
        # Polynomial([0,0,0,...], p) is equal to Polynomial([], p):
        if all(i == 0 for i in self) and other.coefs == [] or all(i == 0 for i in other) and self.coefs == []:
            return True
        return super().__eq__(other)

    @_check_p
    # Polynomial mod p not equal
    def __ne__(self, other):
        """Test if not equal to other PolynomialModP."""
        if all(i == 0 for i in self) and not other or all(i == 0 for i in other) and not self:
            return False
        return super().__ne__(other)

    @_check_p
    def __lt__(self, other):
        super().__lt__(other)

    @_check_p
    def __le__(self, other):
        super().__le__(other)

    @_check_p
    def __gt__(self, other):
        super().__gt__(other)

    @_check_p
    def __ge__(self, other):
        super().__ge__(other)

    # Constant polynomials can be converted to int
    def __int__(self):
        if self.degree() == 0:
            return int(self.coefs[0])
        else:
            raise ValueError("Polynomial is not constant.")

    # Returns polynomial in the canonical notation starting with the highest order term
    def toString(self):
        if not self.coefs:  # If no coefficients
            return "<empty>"
        terms = []
        for i, c in enumerate(reversed(self.coefs)):
            if c != 0 or len(self) == 1:
                term = ""
                if c != 1 or i == 0:
                    term += str(c.n)
                if i > 0:
                    term += "x"
                if i >= 2:
                    term += "^" + str(i)
                terms = [term] + terms
        return " + ".join(terms)

    def __str__(self):
        return "{0} (mod {1})".format(self.toString(), str(self.p))

    def __repr__(self):
        # return "PolynomialModP({0}, {1})".format(str(self.coefs), str(self.p))
        return self.__str__()
