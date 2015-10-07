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
        if type(p) is not int:
            raise ValueError("Argument p is not an integer.")
        if p < 2:
            raise ValueError("Argument p is too small, should be larger than 1.")
        if p > 100:
            raise ValueError("Argument p is too large, should be smaller than 100.")
        if not is_prime(p):
            raise ValueError("Argument p is not actually prime.")
        self.p = p

        self.coefs = []
        skip_zeros = True  # The first * number of zero coefficients should not be included
        # The coefficients are stored from least to most significant
        for c in coefficients:
            if type(c) is not int:
                raise ValueError("Coefficient " + str(c) + " is not an integer.")
            if c != 0 or not skip_zeros:
                self.coefs = [IntegerModP(c, p)] + self.coefs
                skip_zeros = False

                # TODO Test
                # TODO Clean comments/docstring

    # Decorator for all binary operations to check whether primes match
    def _check_p(func):
        def op(self, other):
            if self.p != other.p:
                raise ValueError("Primes are incompatible.")
            return func(self, other)

        return op

    def int_coefs(self):
        """Return coefficients as a reversed list of normal ints"""
        ints = []
        for c in reversed(self.coefs):
            ints.append(int(c))
        return ints

    def degree(self):
        return len(self.coefs) - 1

    # function value of x
    def f(self, x):
        """Return the image of x

        Args:
            x (float): number
        """
        result = 0
        t = 1
        for c in self.coefs:
            result += c.n * t
            t *= x
        return result

    @_check_p
    # Polynomial mod p gcd
    def gcd(self, other):
        """Return the gcd with an other polynomial

        Args:
            other (PolynomialModP): polynomial
        """

        # TODO Implement
        raise NotImplementedError

    # Polynomial mod p congruence with some other polynomial modulo mod
    def congruent(self, other, mod):
        # TODO Implement (use division)
        raise NotImplementedError

    @_check_p
    # Polynomial mod p addition (sum)
    def __add__(self, other):
        result = PolynomialModP([0], self.p)
        for i in range(0, max(self.degree() + 1, other.degree() + 1)):
            try:
                result.coefs.append(self.coefs[i] + other.coefs[i])
            except IndexError:
                if other.degree() <= i:
                    result.coefs.append(self.coefs[i])
                else:
                    result.coefs.append(other.coefs[i])
        return result

    @_check_p
    # Polynomial mod p subtraction (difference)
    def __sub__(self, other):
        result = PolynomialModP([0], self.p)
        for i in range(0, max(self.degree() + 1, other.degree() + 1)):
            try:
                result.coefs.append(self.coefs[i] - other.coefs[i])
            except IndexError:  # The polynomials are not of the same degree
                if other.degree() <= i:
                    result.coefs.append(self.coefs[i])
                else:
                    result.coefs.append(-other.coefs[i])
        return result

    @_check_p
    # Polynomial mod p multiplication (scalar multiple & product)
    def __mul__(self, other):
        result = PolynomialModP([], self.p)
        for i in range(0, len(self.coefs)):
            for j in range(0, len(other.coefs)):
                coefs = [int(self.coefs[i]) * int(other.coefs[j])]
                coefs += (i + j) * [0]  # Pad with i * j zeros to denote it's the (i * j)th term
                result += PolynomialModP(coefs, self.p)
        return result

    @_check_p
    # Polynomial mod p division (longdivide)
    # returns quotient and remainder
    def __truediv__(self, other):
        r = self._clone()  # remainder
        q = PolynomialModP([0], self.p)
        d = other
        while r.degree() > d.degree():
            coefs = r.coefs[-1]
            coefs += (r.degree() - d.degree()) * [0]
            f = PolynomialModP(coefs, self.p)
            r -= f * d
            q += f
        return q, r

    def _clone(self):
        cloned_coefs = []
        for c in self.coefs:
            cloned_coefs += [c.n]
        return PolynomialModP(cloned_coefs, self.p)

    @_check_p
    # Polynomial mod p equal
    def __eq__(self, other):
        if self.degree() != other.degree():
            return False
        for i in range(0, self.degree()):
            if self.coefs[i] != other.coefs[i]:
                return False
        return True

    @_check_p
    # Polynomial mod p not equal
    def __ne__(self, other):
        return not self.__eq__(other)

    def __int__(self):
        if self.degree() == 0:
            return int(self.coefs[0])
        else:
            raise ValueError("Polynomial not constant.")

    def __str__(self):
        return self.__repr__() + " mod " + str(self.p)

    # Represents polynomial in the standard notation starting with the highest order term
    def __repr__(self):
        if not self.coefs:
            return "0"
        repr = self.coefs[0].__repr__()
        for i in range(1, self.degree()):
            if self.coefs[i] != 0:
                repr = self.coefs[i].__repr__() + "x^" + str(i) + " + " + repr
        return repr
