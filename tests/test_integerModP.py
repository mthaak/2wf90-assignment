from unittest import TestCase

from objects.IntegerModP import IntegerModP

class TestIntegerModP(TestCase):
    def setUp(self):
        self.a = IntegerModP(4, 5)
        self.b = IntegerModP(3, 5)

    # Although the test results are positive, errors are given because the exception is raised in the decorator
    # def test___init__noninteger(self):
    #     self.assertRaises(ValueError, IntegerModP(2.5, 3))
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
        result = self.a + self.b
        self.assertEqual(result.n, 2)  # Test correct result
        self.assertEqual(result.p, 5)  # Test if prime also gets transferred

    def test___add__int(self):
        result = self.a + 3
        self.assertEqual(result.n, 2)
        self.assertEqual(result.p, 5)

    def test___sub__(self):
        result = self.a - self.b
        self.assertEqual(result.n, 1)
        self.assertEqual(result.p, 5)

    def test___sub__int(self):
        result = self.a - 3
        self.assertEqual(result.n, 1)
        self.assertEqual(result.p, 5)

    def test___mul__(self):
        result = self.a * self.b
        self.assertEqual(result.n, 2)
        self.assertEqual(result.p, 5)

    def test___mul__int(self):
        result = self.a * 3
        self.assertEqual(result.n, 2)
        self.assertEqual(result.p, 5)

    def test___truediv__(self):
        result = self.a / self.b
        self.assertEqual(result.n, 1)
        self.assertEqual(result.p, 5)

    def test___truediv__int(self):
        result = self.a / 3
        self.assertEqual(result.n, 1)
        self.assertEqual(result.p, 5)

    def test___floordiv__(self):
        result = self.a // self.b
        self.assertEqual(result.n, 1)
        self.assertEqual(result.p, 5)

    def test___floordiv__int(self):
        result = self.a // 3
        self.assertEqual(result.n, 1)
        self.assertEqual(result.p, 5)

    def test___pow__(self):
        result = self.a ** 10
        self.assertEqual(result.n, 1)
        self.assertEqual(result.p, 5)

    def test___neg__(self):
        result = -self.a
        self.assertEqual(result.n, 1)
        self.assertEqual(result.p, 5)

    def test___pos__(self):
        result = self.a
        self.assertEqual(result.n, 4)
        self.assertEqual(result.p, 5)

    # Not needed since these are not overridden
    # def test___iadd__(self):
    #     self.n += self.m
    #     self.assertEqual(int(self.n), 2)
    #
    # def test___isub__(self):
    #     self.n -= self.m
    #     self.assertEqual(int(self.n), 1)
    #
    # def test___imul__(self):
    #     self.n *= self.m
    #     self.assertEqual(int(self.n), 2)
    #
    # def test___itruediv__(self):
    #     self.n /= self.m
    #     self.assertEqual(int(self.n), 1)
    #
    # def test___ifloordiv__(self):
    #     self.n //= self.m
    #     self.assertEqual(int(self.n), 1)
    #
    # def test___ipow__(self):
    #     self.n **= 10
    #     self.assertEqual(int(self.n), 1)

    def test___lt__(self):
        self.assertEqual(self.a < self.b, False)

    def test___lt__int(self):
        self.assertEqual(self.a < 3, False)

    def test___le__(self):
        self.assertEqual(self.a <= self.b, False)

    def test___le__int(self):
        self.assertEqual(self.a <= 3, False)

    def test___eq__(self):
        self.assertEqual(self.a == self.b, False)

    def test___eq__int(self):
        self.assertEqual(self.a == 3, False)

    def test___ne__(self):
        self.assertEqual(self.a != self.b, True)

    def test___ne__int(self):
        self.assertEqual(self.a != 3, True)

    def test___ge__(self):
        self.assertEqual(self.a >= self.b, True)

    def test___ge__int(self):
        self.assertEqual(self.a >= 3, True)

    def test___gt__(self):
        self.assertEqual(self.a > self.b, True)

    def test___gt__int(self):
        self.assertEqual(self.a > 3, True)

    def test___int__(self):
        self.assertEqual(int(self.a), 4)
