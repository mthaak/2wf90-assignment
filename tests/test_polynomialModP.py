from unittest import TestCase
from objects.IntegerModP import IntegerModP

from objects.PolynomialModP import PolynomialModP


class TestPolynomialModP(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.N = PolynomialModP([5, 4, 3, 2, 1], 3)
        cls.L = PolynomialModP([13, 9, 0, 16, 4, 19, 25, 5, 0], 3)
        cls.S = PolynomialModP([0, 4, 0], 3)
        print("N =", cls.N)
        print("L =", cls.L)
        print("S =", cls.S)

    def test___init__intlist(self):
        C = PolynomialModP([3, 2, 1], 5)
        C.coefs = [3, 2, 1]
        C.p = 5

    def test___init__IntegerModPlist(self):
        C = PolynomialModP([IntegerModP(3, 7), IntegerModP(2, 3), IntegerModP(1, 11)], 5)
        C.coefs = [3, 2, 1]
        C.p = 5

    def test___init__comblist(self):
        C = PolynomialModP([IntegerModP(3, 7), 2, IntegerModP(1, 11)], 5)
        C.coefs = [3, 2, 1]
        C.p = 5

    def test___init__notintlist(self):
        with self.assertRaises(ValueError):
            PolynomialModP([1, 3.5, 5], 3)

    def test___init__notinteger_p(self):
        with self.assertRaises(ValueError):
            PolynomialModP([1, 1], 2.5)

    def test___init__notprime_p(self):
        with self.assertRaises(ValueError):
            PolynomialModP([1, 1], 12)

    def test___init__toosmall_p(self):
        with self.assertRaises(ValueError):
            PolynomialModP([1, 1], 1)

    def test___init__toolarge_p(self):
        with self.assertRaises(ValueError):
            PolynomialModP([1, 1], 101)

    def test___check_p(self):
        X = PolynomialModP([1, 2, 3], 5)
        with self.assertRaises(ValueError):
            self.N + X

    def test_clone(self):
        C = self.N.clone()
        self.assertEqual(C.coefs, self.N.coefs)
        self.assertEqual(C.p, self.N.p)
        self.assertEqual(C, self.N)

    def test_int_coefs(self):
        self.assertEqual(self.N.coefs, [2, 1, 0, 2, 1])

    def test_int_coefs_large(self):
        self.assertEqual(self.L.coefs, [1, 0, 0, 1, 1, 1, 1, 2, 0])

    def test_int_coefs_small(self):
        self.assertEqual(self.S.coefs, [1, 0])

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
        self.assertEqual(q.coefs, [1, 0, 1, 1, 1])
        self.assertEqual(q.p, 2)
        self.assertEqual(r.coefs, [0])
        self.assertEqual(r.p, 2)

    def test_gcd_so(self):
        A = PolynomialModP([1, 0, 1, 0, 1], 2)
        B = PolynomialModP([1, 1, 1, 1], 2)
        g, x, y = A.gcd(B)
        self.assertEqual(g, 1)
        self.assertEqual(x * A + y * B, g)

    def test_gcd_large(self):
        g, x, y = self.N.gcd(self.L)
        self.assertEqual(g, 1)
        self.assertEqual(x * self.N + y * self.L, g)

    def test_gcd_small(self):
        g, x, y = self.N.gcd(self.S)
        self.assertEqual(g, 1)
        self.assertEqual(x * self.N + y * self.S, g)

    def test_congruent_large_small(self):
        self.assertIs(self.N.congruent(self.L, self.S), False)

    def test_congruent_large_other(self):
        self.assertIs(self.N.congruent(self.L, PolynomialModP([2, 0, 0, 2, 1, 0, 2, 0, 1], 3)), True)

    def test_congruent_small_large(self):
        self.assertIs(self.N.congruent(self.S, self.L), False)

    def test_congruent_small_other(self):
        self.assertIs(self.N.congruent(self.S, PolynomialModP([2, 1, 0, 1, 1], 3)), True)

    def test_congruent_int_other(self):
        self.assertIs(self.N.congruent(1, PolynomialModP([1, 0], 3)), True)

    def test_congruent_IntegerModP_other(self):
        self.assertIs(self.N.congruent(IntegerModP(1, 3), PolynomialModP([1, 0], 3)), True)

    def test_congruent_PolynomialModP_other(self):
        self.assertIs(self.N.congruent(PolynomialModP([1], 3), PolynomialModP([1, 0], 3)), True)

    def test_congruent_other_int(self):
        self.assertIs(self.N.congruent(PolynomialModP([1, 1, 0, 2], 3), 2), True)

    def test_congruent_other_IntegerModP(self):
        self.assertIs(self.N.congruent(PolynomialModP([1, 1, 0, 2], 3), IntegerModP(2, 3)), True)

    def test_congruent_other_PolynomialModP(self):
        self.assertIs(self.N.congruent(PolynomialModP([1, 1, 0, 2], 3), PolynomialModP([2], 3)), True)

    def test___add__large(self):
        result = self.N + self.L
        self.assertEqual(result.coefs, [1, 0, 0, 1, 0, 2, 1, 1, 1])
        self.assertEqual(result.p, 3)
        self.assertEqual(result, PolynomialModP([1, 0, 0, 1, 0, 2, 1, 1, 1], 3))

    def test___add__small(self):
        result = self.N + self.S
        self.assertEqual(result.coefs, [2, 1, 0, 0, 1])
        self.assertEqual(result.p, 3)

    def test___sub__large(self):
        result = self.N - self.L
        self.assertEqual(result.coefs, [2, 0, 0, 2, 1, 0, 2, 0, 1])
        self.assertEqual(result.p, 3)

    def test___sub__small(self):
        result = self.N - self.S
        self.assertEqual(result.coefs, [2, 1, 0, 1, 1])
        self.assertEqual(result.p, 3)

    def test___mul__large(self):
        result = self.N * self.L
        self.assertEqual(result.coefs, [2, 1, 0, 1, 1, 0, 2, 2, 2, 0, 2, 2, 0])
        self.assertEqual(result.p, 3)

    def test___mul__small(self):
        result = self.N * self.S
        self.assertEqual(result.coefs, [2, 1, 0, 2, 1, 0])
        self.assertEqual(result.p, 3)

    def test___mul__int(self):
        result = self.N * 3
        self.assertEqual(result.coefs, [0])
        self.assertEqual(result.p, 3)

    def test___mul__int_small(self):
        result = self.S * 4
        self.assertEqual(result.coefs, [1, 0])
        self.assertEqual(result.p, 3)

    def test___mul__int_large(self):
        result = self.L * 2
        self.assertEqual(result.coefs, [2, 0, 0, 2, 2, 2, 2, 1, 0])
        self.assertEqual(result.p, 3)

    def test___truediv__large(self):
        result = self.N / self.L
        self.assertEqual(result.coefs, [0])
        self.assertEqual(result.p, 3)

    def test___truediv__small(self):
        result = self.N / self.S
        self.assertEqual(result.coefs, [2, 1, 0, 2])
        self.assertEqual(result.p, 3)

    def test___mod__large(self):
        result = self.N % self.L
        self.assertEqual(result.coefs, [2, 1, 0, 2, 1])
        self.assertEqual(result.p, 3)

    def test___mod__small(self):
        result = self.N % self.S
        self.assertEqual(result.coefs, [1])
        self.assertEqual(result.p, 3)

    def test___pow__(self):
        result = self.N ** 3
        self.assertEqual(result.coefs, [2, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 1])
        self.assertEqual(result.p, 3)

    def test___pow__small(self):
        result = self.S ** 4
        self.assertEqual(result.coefs, [1, 0, 0, 0, 0])
        self.assertEqual(result.p, 3)

    def test___pow__large(self):
        result = self.L ** 0
        self.assertEqual(result, 1)
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
        I = PolynomialModP([5], 7)
        self.assertEqual(type(int(I)), int)
        self.assertEqual(int(I), 5)

    def test___int__error(self):
        with self.assertRaises(ValueError):
            int(self.N)

    def test_1_1b(self):
        A = PolynomialModP([1, 0, 1], 2)
        B = PolynomialModP([1, 0, 0, 1], 2)
        g, x, y = A.gcd(B)
        self.assertEqual(g, PolynomialModP([1, 1], 2))
        self.assertEqual(x * A + y * B, g)

    def test_1_1c(self):
        A = PolynomialModP([1, -1, 1], 3)
        B = PolynomialModP([1, 0, 1, 2], 3)
        g, x, y = A.gcd(B)
        self.assertEqual(g, PolynomialModP([1, -2], 3))
        self.assertEqual(x * A + y * B, g)

    def test_1_8(self):
        A = PolynomialModP([1, -1], 7)
        B = PolynomialModP([1, 1, 1], 7)
        g, x, y = A.gcd(B)
        self.assertEqual(g, PolynomialModP([3], 7))
        self.assertEqual(x * A + y * B, g)

    def test_2_1a(self):
        result = PolynomialModP([1, 0, 0, 0], 7).congruent(1, PolynomialModP([1, 1, 1], 7))
        self.assertEqual(result, True)

    def test_2_1b(self):
        result = PolynomialModP([1, 0, 0, 1, 2], 5).congruent(PolynomialModP([1, 3], 5), PolynomialModP([1, 1], 5))
        self.assertEqual(result, True)

    def test_3_6a(self):
        result = PolynomialModP([1, 0, 0, 1, 1], 2) / PolynomialModP([1, 1, 1], 2)
        self.assertEqual(result, PolynomialModP([1, 1, 0], 2))
        result = PolynomialModP([1, 0, 0, 1, 1], 2) % PolynomialModP([1, 1, 1], 2)
        self.assertEqual(result, 1)

    def test_3_10(self):
        result = PolynomialModP([1, 0, 0, 0, 1, 1], 2) / PolynomialModP([1, 1, 1], 2)
        self.assertEqual(result, PolynomialModP([1, 1, 0, 1], 2))
        result = PolynomialModP([1, 0, 0, 0, 1, 1], 2) % PolynomialModP([1, 1, 1], 2)
        self.assertEqual(result, 0)

    def test_3_11(self):
        result = PolynomialModP([1, 0, 0, 0, 0, 0, 0, 0], 2) / PolynomialModP([1, 0, 1, 1], 2)
        self.assertEqual(result, PolynomialModP([1, 0, 1, 1, 1], 2))
        result = PolynomialModP([1, 0, 0, 0, 0, 0, 0, 0], 2) % PolynomialModP([1, 0, 1, 1], 2)
        self.assertEqual(result, PolynomialModP([1], 2))
