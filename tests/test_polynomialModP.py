from unittest import TestCase

from objects.PolynomialModP import PolynomialModP


class TestPolynomialModP(TestCase):
    def setUp(self):
        self.N = PolynomialModP([5, 4, 3, 2, 1], 3)
        self.L = PolynomialModP([13, 9, 0, 16, 4, 19, 25, 5, 0], 3)
        self.S = PolynomialModP([0, 4, 0], 3)
        self.I = PolynomialModP([5], 3)
        print("N =", self.N)
        print("L =", self.L)
        print("S =", self.S)
        # TODO test with empty polynomial

    def _to_intlist(self, list):
        intlist = []
        for i in list:
            intlist += [int(i)]
        return list(reversed(intlist))

    def test___init__nonintlist(self):
        self.assertRaises(ValueError, PolynomialModP([1.7, 3.5, 5.4], 3))

    def test___init__empty(self):
        self.assertRaises(ValueError, PolynomialModP([], 3))

    def test__check_p(self):
        X = PolynomialModP([1, 2, 3], 4)
        self.assertRaises(ValueError, self.N + X)

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

    def test_gcd_large(self):
        self.assertEqual(self.N.gcd(self.L).int_coefs(), [1])

    def test_gcd_small(self):
        self.assertEqual(self.N.gcd(self.S).int_coefs(), [1])

    def test_congruent_large(self):
        self.assertTrue(False)

    def test_congruent_small(self):
        self.assertTrue(False)

    def test___add__large(self):
        result = self.N + self.L
        self.assertEqual(result.int_coefs(), [1, 0, 0, 1, 0, 2, 1, 1, 1])
        self.assertEqual(result.p, 3)

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
        pass

    def test___mul__small(self):
        result = self.N * self.S
        self.assertEqual(result.int_coefs(), [2, 1, 0, 2, 1, 0])
        self.assertEqual(result.p, 3)
        pass

    def test___truediv__(self):
        C = PolynomialModP([1, 0, 0, 0, 0, 0, 0, 1], 2)
        D = PolynomialModP([1, 0, 1, 1], 2)
        expected_q = PolynomialModP([1, 1, 1, 1], 3)
        expected_r = PolynomialModP([0], 3)
        result = C / D
        self.assertEqual(result.r, expected_r)
        self.assertEqual(result.q, expected_q)

    def test___truediv__large(self):
        result = self.N / self.L
        self.assertEqual(result.r.int_coefs(), [13, 9, 0, 16, 4, 19, 25, 5, 0])
        self.assertEqual(result.r.p, 3)
        self.assertEqual(result.q.int_coefs(), [])
        self.assertEqual(result.q.p, 3)

    def test___truediv__small(self):
        result = self.N / self.S
        self.assertEqual(result.r.int_coefs(), [2, 2, 0, 0])
        self.assertEqual(result.r.p, 3)
        self.assertEqual(result.q.int_coefs(), [1])
        self.assertEqual(result.q.p, 3)
        pass

    def test___eq__equal(self):
        self.assertEqual(self.N == self.N, True)

    def test___eq__nonequal_large(self):
        self.assertEqual(self.N == self.L, False)

    def test___eq__nonequal_small(self):
        self.assertEqual(self.N == self.S, False)

    def test___ne__equal(self):
        self.assertEqual(self.N != self.N, False)

    def test___ne__nonequal_large(self):
        self.assertEqual(self.N != self.L, True)

    def test___ne__nonequal_small(self):
        self.assertEqual(self.N != self.S, True)

    def test___int__error(self):
        self.assertRaises(ValueError, int(self.N))

    def test___int__(self):
        print(self.I.degree())
        self.assertEqual(int(self.I), 2)
