from unittest import TestCase

from objects.PolynomialModP import PolynomialModP


class TestPolynomialModP(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.N = PolynomialModP([5, 4, 3, 2, 1], 3)
        cls.L = PolynomialModP([13, 9, 0, 16, 4, 19, 25, 5, 0], 3)
        cls.S = PolynomialModP([0, 4, 0], 3)
        cls.I = PolynomialModP([5], 3)
        print("N =", cls.N)
        print("L =", cls.L)
        print("S =", cls.S)
        print("I =", cls.I)
        # TODO more testing (e.g. more combinations of types)

    def test___init__notintlist(self):
        with self.assertRaises(ValueError):
            PolynomialModP([1.7, 3.5, 5.4], 3)

    def test___check_p(self):
        X = PolynomialModP([1, 2, 3], 5)
        with self.assertRaises(ValueError):
            self.N + X

    def test_int_coefs(self):
        self.assertEqual(self.N.int_coefs(), [2, 1, 0, 2, 1])

    def test_int_coefs_large(self):
        self.assertEqual(self.L.int_coefs(), [1, 0, 0, 1, 1, 1, 1, 2, 0])

    def test_int_coefs_small(self):
        self.assertEqual(self.S.int_coefs(), [1, 0])

    def test_degree(self):
        self.assertEqual(self.N.degree(), 4)

    def test_degree_large(self):
        self.assertEqual(self.L.degree(), 8)

    def test_degree_small(self):
        self.assertEqual(self.S.degree(), 1)

    def test_f(self):
        self.assertEqual(self.N.f(3.5), 351)

    def test_f_large(self):
        self.assertEqual(self.L.f(7), 5784415)

    def test_f_small(self):
        self.assertEqual(self.S.f(4), 4)

    def test_longdivide(self):
        C = PolynomialModP([1, 0, 0, 0, 0, 0, 0, 1], 2)
        D = PolynomialModP([1, 0, 1, 1], 2)
        q, r = C.long_divide(D)
        self.assertEqual(q.int_coefs(), [1, 0, 1, 1, 1])
        self.assertEqual(q.p, 2)
        self.assertEqual(r.int_coefs(), [])
        self.assertEqual(r.p, 2)

    def test_gcd_large(self):
        self.assertEqual(self.N.gcd(self.L).int_coefs(), [1])

    def test_gcd_small(self):
        self.assertEqual(self.N.gcd(self.S).int_coefs(), [1])

    def test_congruent(self):
        self.assertIs(self.N.congruent(self.L, self.S), False)

    def test___add__large(self):
        result = self.N + self.L
        self.assertEqual(result.int_coefs(), [1, 0, 0, 1, 0, 2, 1, 1, 1])
        self.assertEqual(result.p, 3)
        self.assertEqual(result, PolynomialModP([1, 0, 0, 1, 0, 2, 1, 1, 1], 3))

    def test___add__small(self):
        result = self.N + self.S
        self.assertEqual(result.int_coefs(), [2, 1, 0, 0, 1])
        self.assertEqual(result.p, 3)

    def test___sub__large(self):
        result = self.N - self.L
        self.assertEqual(result.int_coefs(), [2, 0, 0, 2, 1, 0, 2, 0, 1])
        self.assertEqual(result.p, 3)

    def test___sub__small(self):
        result = self.N - self.S
        self.assertEqual(result.int_coefs(), [2, 1, 0, 1, 1])
        self.assertEqual(result.p, 3)

    def test___mul__large(self):
        result = self.N * self.L
        self.assertEqual(result.int_coefs(), [2, 1, 0, 1, 1, 0, 2, 2, 2, 0, 2, 2, 0])
        self.assertEqual(result.p, 3)

    def test___mul__small(self):
        result = self.N * self.S
        self.assertEqual(result.int_coefs(), [2, 1, 0, 2, 1, 0])
        self.assertEqual(result.p, 3)

    def test___mul__int(self):
        result = self.N * 3
        self.assertEqual(result.int_coefs(), [])
        self.assertEqual(result.p, 3)

    def test___mul__int_small(self):
        result = self.S * 4
        self.assertEqual(result.int_coefs(), [1, 0])
        self.assertEqual(result.p, 3)

    def test___mul__int_large(self):
        result = self.L * 2
        self.assertEqual(result.int_coefs(), [2, 0, 0, 2, 2, 2, 2, 1, 0])
        self.assertEqual(result.p, 3)

    def test___truediv__large(self):
        result = self.N / self.L
        self.assertEqual(result.int_coefs(), [0])
        self.assertEqual(result.p, 3)

    def test___truediv__small(self):
        result = self.N / self.S
        self.assertEqual(result.int_coefs(), [2, 1, 0, 2])
        self.assertEqual(result.p, 3)

    def test___mod__large(self):
        result = self.N % self.L
        self.assertEqual(result.int_coefs(), [2, 1, 0, 2, 1])
        self.assertEqual(result.p, 3)

    def test___mod__small(self):
        result = self.N % self.S
        self.assertEqual(result.int_coefs(), [1])
        self.assertEqual(result.p, 3)

    def test___eq__equal(self):
        self.assertEqual(self.N == self.N, True)

    def test___eq__notequal_large(self):
        self.assertEqual(self.N == self.L, False)

    def test___eq__notequal_small(self):
        self.assertEqual(self.N == self.S, False)

    def test___ne__equal(self):
        self.assertEqual(self.N != self.N, False)

    def test___ne__notequal_large(self):
        self.assertEqual(self.N != self.L, True)

    def test___ne__notequal_small(self):
        self.assertEqual(self.N != self.S, True)

    def test___len__(self):
        self.assertEqual(len(self.N), 5)

    def test___len__large(self):
        self.assertEqual(len(self.L), 9)

    def test___len__small(self):
        self.assertEqual(len(self.S), 2)

    def test___int__(self):
        self.assertEqual(int(self.I), 2)

    def test___int__error(self):
        with self.assertRaises(ValueError):
            int(self.N)
