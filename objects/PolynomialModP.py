from common import *
from objects.IntegerModP import IntegerModP
import itertools


class PolynomialModP(list):
    """Polynomial mod prime p

    Attributes:
        coefs (list): list of IntegerModP, sorted from least to most significant
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
        for c in coefficients:
            if c % p != 0 or not skip_zeros or len(coefficients) == 1:
                # all coefficients are forced modulo of p
                if type(c) is IntegerModP:
                    coefs = [IntegerModP(c.n % p, p)] + coefs
                elif type(c) is int:
                    coefs = [IntegerModP(c, p)] + coefs  # int is converted to IntegerModP
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
        def op(self, other):
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
            return func(self, other)

        return op

    # Clone self to prevent mutation
    def _clone(self):
        """Clone self."""
        return PolynomialModP(self.int_coefs(), self.p)

    def int_coefs(self):
        """Return coefficients as a list of int, sorted from most to least significant."""
        return list(map(int, reversed(self.coefs)))

    def degree(self):
        """Return the degree."""
        return len(self.coefs) - 1

    # Function value of x
    def f(self, x):
        """Return the image of x."""
        result = 0
        t = 1  # term
        for c in self.coefs:
            result += c.n * t
            t *= x
        return result

    @_check_p
    # Long division
    def long_divide(self, other):
        """Long divide by other PolynomialModP, returns (quotient, remainder) as tuple."""
        q = PolynomialModP([0], self.p)  # quotient
        r = self._clone()  # remainder
        d = other  # divisor
        while r.degree() >= d.degree() and r != 0:
            f_coefs = [int(r.coefs[-1] / d.coefs[-1])]
            f_coefs += (r.degree() - d.degree()) * [0]  # Pad with zero's to denote term
            f = PolynomialModP(f_coefs, self.p)  # factor
            r -= f * d
            q = q + f
        return q, r

    @_check_p
    # Polynomial mod p gcd using Euclidian algorithm
    def gcd(self, other):
        """Calculate the gcd with other PolynomialModP."""
        a = self._clone()
        b = other._clone()
        while b > [1]:
            a, b = b, a % b
        return a if not b else PolynomialModP([1], self.p)
        # def gcd_rec(a, b):
        #     if a == PolynomialModP([0], self.p):
        #         return b
        #     else:
        #         q, r = b / a
        #         return gcd_rec(r, a)
        #
        # return gcd_rec(a, b)

    # Polynomial mod p congruence with other polynomial modulo mod
    def congruent(self, other, k):
        """Test congruence with other PolynomialModP (mod k)"""
        return (self - other) % k == 0

    @_check_p
    # Polynomial mod p addition (sum)
    def __add__(self, other):
        """Add other PolynomialModP."""
        coefs = [(i + j) % self.p for i, j in itertools.zip_longest(self, other, fillvalue=0)]
        return PolynomialModP(list(reversed(coefs)), self.p)  # init requires int list in reverse

    # Makes add operation commutative, result is in both cases a PolynomialModP
    def __radd__(self, other):
        return self.__add__(other)

    @_check_p
    # Polynomial mod p subtraction (difference)
    def __sub__(self, other):
        """Subtract other PolynomialModP."""
        coefs = [(i - j) % self.p for i, j in itertools.zip_longest(self, other, fillvalue=0)]
        return PolynomialModP(list(reversed(coefs)), self.p)

    # Makes subtract operation commutative
    def __rsub__(self, other):
        return self.__rsub__(other)

    @_check_p
    # Polynomial mod p multiplication (scalar multiple & product)
    def __mul__(self, other):
        """Multiply with other PolynomialModP (or IntegerModP/int for scalar multiple)."""
        coefs = [0] * (self.degree() + other.degree() + 1)
        for i in range(0, len(self)):
            for j in range(0, len(other)):
                coefs[i + j] += int(self.coefs[i]) * int(other.coefs[j])
                coefs[i + j] %= self.p
        return PolynomialModP(list(reversed(coefs)), self.p)

    # Makes multiply operation commutative
    def __rmul__(self, other):
        return self.__rmul__(other)

    # Division operation makes use of long division
    def __truediv__(self, other):
        """Divide by other PolynomialModP."""
        return self.long_divide(other)[0]

    # Modulo operation makes use of long division
    def __mod__(self, other):
        """Modulo by other PolynomialModP."""
        return self.long_divide(other)[1]

    #
    def __pow__(self, power):
        if power == 0:
            return PolynomialModP([0], self.p)
        elif power == 1:
            return self
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

    # Constant polynomials can be converted to int
    def __int__(self):
        if self.degree() == 0:
            return int(self.coefs[0])
        else:
            raise ValueError("Polynomial is not constant.")

    # Returns polynomial in the canonical notation starting with the highest order term
    def __str__(self):
        if not self.coefs:  # If no coefficients
            return "<null> (mod " + str(self.p) + ")"
        terms = []
        for i in range(0, len(self.coefs)):
            if self.coefs[i] != 0 or len(self) == 1:
                term = ""
                if self.coefs[i] != 1 or i == 0:
                    term += str(self.coefs[i].n)
                if i > 0:
                    term += "x"
                if i >= 2:
                    term += "^" + str(i)
                terms = [term] + terms

        return "{0} (mod {1})".format(" + ".join(terms), str(self.p))

    def __repr__(self):
        return "PolynomialModP({0}, {1})".format(str(self.int_coefs()), str(self.p))
