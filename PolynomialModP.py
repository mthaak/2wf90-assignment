import IntegerModP


class PolynomialModP():
    def __init__(self, prime, *coefficients):
        self.p = prime

        self.coefs = []
        for c in coefficients:
            self.coefs.append(IntegerModP(c, prime))

    def terms(self):
        return self.coefs.size()

    def sum(self, q):
        pass

    def scalarMultiple(self, q):
        pass

    def difference(self, q):
        pass

    def product(self, q):
        pass

    def longDivide(self, q):
        pass
