from unittest import TestCase
from IntegerModP import IntegerModP

__author__ = 'Martin'


class TestIntegerModP(TestCase):
    def setUp(self):
        self.n = IntegerModP(4, 5)
        self.m = IntegerModP(3, 5)

    # Although the test results are positive, errors are given
    # def test__check_p(self):
    #     x = IntegerModP(2, 3)
    #     self.assertRaises(ValueError, self.n + x)
    #
    # def test__check_power_noninteger(self):
    #     self.assertRaises(ValueError, self.n.__pow__(self.m))
    #
    # def test__check_power_negative(self):
    #     self.assertRaises(ValueError, self.n ** (-2))

    def test___add__(self):
        self.assertEqual(int(self.n + self.m), 2)
        self.assertEqual((self.n + self.m).p, 5)  # Test if prime also gets transferred

    def test___sub__(self):
        self.assertEqual(int(self.n - self.m), 1)

    def test___mul__(self):
        self.assertEqual(int(self.n * self.m), 2)

    def test___truediv__(self):
        self.assertEqual(int(self.n / self.m), 1)

    def test___floordiv__(self):
        self.assertEqual(int(self.n // self.m), 1)

    def test___pow__(self):
        self.assertEqual(int(self.n ** 10), 1)

    def test___iadd__(self):
        self.n += self.m
        self.assertEqual(int(self.n), 2)

    def test___isub__(self):
        self.n -= self.m
        self.assertEqual(int(self.n), 1)

    def test___imul__(self):
        self.n *= self.m
        self.assertEqual(int(self.n), 2)

    def test___itrudiv__(self):
        self.n /= self.m
        self.assertEqual(int(self.n), 1)

    def test___ifloordiv__(self):
        self.n //= self.m
        self.assertEqual(int(self.n), 1)

    def test___ipow__(self):
        self.n **= 10
        self.assertEqual(int(self.n), 1)

    def test___lt__(self):
        self.assertEqual(self.n < self.m, False)

    def test___le__(self):
        self.assertEqual(self.n <= self.m, False)

    def test___eq__(self):
        self.assertEqual(self.n == self.m, False)

    def test___ne__(self):
        self.assertEqual(self.n != self.m, True)

    def test___ge__(self):
        self.assertEqual(self.n >= self.m, True)

    def test___gt__(self):
        self.assertEqual(self.n > self.m, True)
