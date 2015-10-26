import itertools
from math import log, floor
from common import *
from objects.IntegerModP import IntegerModP
from objects.PolynomialModP import PolynomialModP


class FiniteField:
    def __init__(self, f, p):
        if type(f) is list:
            f = PolynomialModP(f, p)  # Polynomial gets mod p of field
        elif type(f) is PolynomialModP:
            f.p = p  # Polynomial gets mod p of field
        else:
            raise ValueError("Argument f type " + str(type(f)) + " is not supported.")

        if type(p) is not int:
            raise ValueError("Argument p is not an integer.")
        if p < 2:
            raise ValueError("Argument p is too small, should be larger than 1.")
        if p > 100:
            raise ValueError("Argument p is too large, should be smaller than 100.")
        if not is_prime(p):
            raise ValueError("Argument p is not actually prime.")
        self.p = p

        if f.degree() > 1 and not self.isIrreducible(f) \
                or f.degree() == 1 and f.coefs[1] == 0:
            raise ValueError("Argument f is not irreducible.")
        if f.degree() == 0:
            raise ValueError("Argument f can not be constant.")
        self.f = f

    # Decorator for all binary operations to check and convert argument types if needed
    def _check_args(func):
        def op(self, a, b):
            if type(a) is list:
                a = PolynomialModP(a, self.p)
            elif type(a) is PolynomialModP:
                a = PolynomialModP(a.coefs, self.p)  # Gets mod p of field
            else:
                raise ValueError("Operand type " + str(type(a)) + "is not supported.")
            if type(b) is list:
                b = PolynomialModP(b, self.p)
            elif type(b) is PolynomialModP:
                b = PolynomialModP(b.coefs, self.p)  # Gets mod p of field
            else:
                raise ValueError("Operand type " + str(type(b)) + "is not supported.")
            return func(self, a, b)

        return op

    # Decorator for operation with one argument
    def _check_arg(func):
        def op(self, a, *args):
            if type(a) is list:
                a = PolynomialModP(a, self.p)
            elif type(a) is PolynomialModP:
                a = PolynomialModP(a.coefs, self.p)  # Gets mod p of field
            else:
                raise ValueError("Operand type " + str(type(a)) + "is not supported.")
            return func(self, a, *args)

        return op

    def additionTable(self):
        """Print addition table."""
        print(self.Table([[i + j for i in self.elements()] for j in self.elements()], self.elements(), "+"))

    def multiplicationTable(self):
        """Print multiplication table."""
        print(self.Table([[i * j for i in self.elements()] for j in self.elements()], self.elements(), "*"))

    def elements(self):
        """Get residue classes in field."""
        return [PolynomialModP(list(f), self.p) for f in
                itertools.product(list(range(0, self.p)), repeat=self.f.degree())]

    @_check_arg
    def isPrimitive(self, a):
        """Test primitivity of element a."""
        # Algorithm 3.4.3
        i = 1
        q = self.p
        p = prime_divisors(q - 1)
        n = len(p)
        e = a ** ((q - 1) / p[i - 1])
        while i <= n and a ** ((q - 1) / p[i - 1]) != 1:
            i += 1
        return False if i <= n else True

    def primitiveElement(self):
        """Find primitive element in field."""
        # Algorithm 3.4.4
        for a in [e for e in self.elements() if e.degree() > 0]:
            if self.isPrimitive(a):
                return a
        raise RuntimeError("No primitive element found.")

    @_check_arg
    def isIrreducible(self, f):
        """Test irreducibility of element f."""
        # Algorithm 4.1.4
        t = 1
        n = f.degree()
        if n <= 1:
            raise ValueError("Polynomial f should be of degree > 1.")
        while f.gcd(PolynomialModP([1, 0], self.p) ** (self.p ** t) - PolynomialModP([1, 0], self.p))[0].degree() == 0:
            t += 1
        return t == n

    def irreducibleElement(self, n):
        """Find irreducible element of degree n in field."""
        # Algorithm 4.1.6
        if type(n) is not int:
            raise ValueError("Degree n should be of type int.")
        if n <= 0:
            raise ValueError("Degree n should be > 0.")
        polynomials = [PolynomialModP(list(f), self.p) for f in
                       itertools.product(list(range(0, self.p)), repeat=self.f.degree() + 1)]
        polynomials_deg_n = [p for p in polynomials if p.degree() == n]
        for p in polynomials_deg_n:
            if self.isIrreducible(p):
                return p
        raise RuntimeError("No irreducible element found.")

    @_check_args
    def sum(self, a, b):
        """Calculate the sum of field elements a and b."""
        return (a + b) % self.f

    @_check_args
    def product(self, a, b):
        """Calculate the product of field elements a and b."""
        return (a * b) % self.f

    @_check_args
    def quotient(self, a, b):
        """Calculate the quotient of field elements a and b."""
        # return (a / b) % self.f
        return (a * self.inverse(b)) % self.f

    @_check_arg
    def inverse(self, a):
        """Calculate inverse of field element a."""
        # Algorithm 2.3.3
        d, x, y = self.f.gcd(a)
        if d == 1:
            return x + d
        else:
            raise ValueError("a + (d) is not invertible")

    @_check_arg
    def exp_basis(self, a, m):
        """Calculate a to the power m using a normal basis."""
        i = 0
        k = floor(log(m, 2))
        m = [int(x) for x in reversed(bin(m)[2:])]
        # if m[0] == 0:
        #     g = 1
        # else:
        #     g = PolynomialModP([1], a.p) % a
        g = PolynomialModP([1], a.p)
        while i <= k:
            g = g ** 2 % self.f
            if m[i] == 1:
                g = (g * a) % self.f
            i += 1
        return g

    def __str__(self):
        return "Z/{0}Z[X] / ({1})".format(str(self.p), self.f.toString())

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.elements())

    class Table:
        def __init__(self, m, e, op):
            self.table = m  # resulting table of operation
            self.elems = e  # operands
            self.op = op  # operation

        def __str__(self):
            n_columns = 1 + len(self.table)  # number of columns
            full_table = \
                [[self.op] + [e.toString() for e in self.elems]] + \
                [[self.elems[i].toString()] + [item.toString() for item in row] for i, row in enumerate(self.table)]
            # Calculates width of each column using widest element
            column_widths = [max([len(row[i]) for row in full_table]) for i in range(n_columns)]
            row_strings = []
            for row in full_table:
                row_strings.append(" | ".join([row[i].ljust(column_widths[i]) for i in range(n_columns)]))
            row_strings.insert(1, "-+-".join(["-" * column_widths[i] for i in range(n_columns)]))  # border
            return "\n".join(row_strings)
