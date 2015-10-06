from unittest import TestCase

from objects.PolynomialModP import PolynomialModP


class TestPolynomialModP(TestCase):
    def setUp(self):
        self.N = PolynomialModP([5, 4, 3, 2, 1], 3)
        self.L = PolynomialModP([13, 9, 0, 16, 4, 19, 25, 5, 0], 3)
        self.S = PolynomialModP([0, 4, 0], 3)
        pass

    def test___init__nonintlist(self):
        self.assertRaises(ValueError, PolynomialModP([1.7, 3.5, 5.4], 3))

    def test___init__empty(self):
        self.assertRaises(ValueError, PolynomialModP([], 3))

    def test__check_p(self):
        X = PolynomialModP([1, 2, 3], 4)
        self.assertRaises(ValueError, self.N + X)

    def test_terms_large(self):
        self.assertEqual(self.L.terms(), 9)

    def test_terms_small(self):
        self.assertEqual(self.S.terms(), 2)

    def test_f_large(self):
        # TODO
        pass

    def test_f_small(self):
        # TODO
        pass

    def test_gcd_large(self, other):
        # TODO
        pass

    def test_gcd_small(self, other):
        # TODO
        pass

    def test___add__large(self):
        expected = [1, 0, 0, 1, 0, 2, 1, 1, 0]
        self.assertEqual((self.N + self.L).coefs, expected)

    def test___add__small(self):
        expected = [5, 4, 3, 0, 1]
        self.assertEqual((self.N + self.S).coefs, expected)

    def test___sub__large(self):
        expected = [2, 0, 0, 2, 1, 0, 2, 0, 1]
        self.assertEqual((self.N - self.L).coefs, expected)

    def test___sub__small(self):
        expected = [5, 4, 3, 1, 1]
        self.assertEqual((self.N - self.S).coefs, expected)

    def test___mul__large(self):
        # TODO
        pass

    def test___mul__small(self):
        # TODO
        pass

    def test___truediv__large(self):
        # TODO
        pass

    def test___truediv__small(self):
        # TODO
        pass

    def test___eq__equal(self):
        self.assertEqual(self.N == self.N, True)

    def test___eq__nonequal_large(self):
        self.assertEqual(self.N == self.M, False)

    def test___eq__nonequal_small(self):
        self.assertEqual(self.N == self.S, False)

    def test___ne__equal(self):
        self.assertEqual(self.N != self.N, False)

    def test___ne__nonequal_large(self):
        self.assertEqual(self.N != self.M, True)

    def test___ne__nonequal_small(self):
        self.assertEqual(self.N != self.S, True)
