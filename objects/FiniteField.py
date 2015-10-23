import itertools
from common import *
from objects.IntegerModP import IntegerModP
from objects.PolynomialModP import PolynomialModP


def prime_divisors(n):
    divisors = [d for d in range(2, n // 2 + 1) if n % d == 0]
    return [d for d in divisors if all(d % od != 0 for od in divisors if od != d)] + [n]


class FiniteField:
    def __init__(self, f, p):
        # TODO test irreducibility of f
        self.f = f

        if type(p) is not int:
            raise ValueError("Argument p is not an integer.")
        if p < 2:
            raise ValueError("Argument p is too small, should be larger than 1.")
        if p > 100:
            raise ValueError("Argument p is too large, should be smaller than 100.")
        if not is_prime(p):
            raise ValueError("Argument p is not actually prime.")
        self.p = p

    def additionTable(self):
        return self.Table([[i + j for i in self.elements()] for j in self.elements()], self.elements(), "+")

    def multiplicationTable(self):
        return self.Table([[i * j for i in self.elements()] for j in self.elements()], self.elements(), "*")

    def elements(self):
        return [PolynomialModP(list(f), self.p) for f in
                itertools.product(list(range(0, self.p)), repeat=self.f.degree())]

    def isPrimitive(self, a):
        # Algorithm 3.4.3
        i = 1
        q = self.p
        p = prime_divisors(q - 1)
        n = len(p)
        e = a ** ((q - 1) / p[i - 1])
        while i <= n and a ** ((q - 1) / p[i - 1]) != 1:
            i += 1
        return False if i <= n else True

    def isIrreducible(self, f):
        # Algorithm 4.1.4
        t = 1
        n = f.degree()
        while f.gcd(PolynomialModP([1], self.p) - PolynomialModP([1], self.p)) == 1:
            t += 1
        return t == n

    def primitiveElement(self):
        # Algorithm 3.4.4
        for a in self.elements()[1:]:
            if self.isPrimitive(a):
                return a
        raise RuntimeError("No primitive element found.")

    def sum(self, a, b):
        return PolynomialModP(a, self.p) + PolynomialModP(b, self.p)

    def product(self, a, b):
        return PolynomialModP(a, self.p) * PolynomialModP(b, self.p)

    def quotient(self, a, b):
        return PolynomialModP(a, self.p) / PolynomialModP(b, self.p)
        # TODO use inverse

    def __str__(self):
        pass

    def __repr__(self):
        # pass
        return self.__str__()

    def __len__(self):
        return len(self.elements())

    class Table:
        def __init__(self, m, e, op):
            self.table = m  # resulting table of operation
            self.elems = e  # operands
            self.op = op  # operation

        def __str__(self):
            n_columns = 1 + len(self.table)
            full_table = \
                [[self.op] + [e.toString() for e in self.elems]] + \
                [[self.elems[i].toString()] + [item.toString() for item in row] for i, row in enumerate(self.table)]
            column_widths = [max([len(row[i]) for row in full_table]) for i in range(n_columns)]
            row_strings = []
            for row in full_table:
                row_strings.append(" | ".join([row[i].ljust(column_widths[i]) for i in range(n_columns)]))
            row_strings.insert(1, "-+-".join(["-" * column_widths[i] for i in range(n_columns)]))  # border
            return "\n".join(row_strings)
