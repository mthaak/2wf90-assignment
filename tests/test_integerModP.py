from unittest import TestCase

from objects.IntegerModP import IntegerModP


class TestIntegerModP(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a = IntegerModP(4, 5)
        cls.b = IntegerModP(3, 5)
        print("a =", str(cls.a))
        print("b =", str(cls.b))
        # TODO more testing (e.g. more combinations of types)

    def test___init__(self):
        c = IntegerModP(2, 5)
        self.assertEqual(c.n, 2)
        self.assertEqual(c.p, 5)

    def test___init__notinteger(self):
        with self.assertRaises(ValueError):
            IntegerModP(2.5, 3)

    def test___check_p(self):
        x = IntegerModP(2, 3)
        with self.assertRaises(ValueError):
            self.a + x

    def test__check_power_negative(self):
        with self.assertRaises(ValueError):
            self.a ** -2

    def test___add__(self):
        result = self.a + self.b
        self.assertEqual(result.n, 2)  # Test correct result
        self.assertEqual(result.p, 5)  # Test if prime also gets transferred

    def test___add__int_r(self):
        result = self.a + 3
        self.assertEqual(result.n, 2)
        self.assertEqual(result.p, 5)

    def test___add__int_l(self):
        result = 3 + self.a
        self.assertEqual(result, 7)

    def test___sub__(self):
        result = self.a - self.b
        self.assertEqual(result.n, 1)
        self.assertEqual(result.p, 5)

    def test___sub__int_r(self):
        result = self.a - 3
        self.assertEqual(result.n, 1)
        self.assertEqual(result.p, 5)

    def test___sub__int_l(self):
        result = 3 - self.a
        self.assertEqual(result, -1)

    def test___mul__(self):
        result = self.a * self.b
        self.assertEqual(result.n, 2)
        self.assertEqual(result.p, 5)

    def test___mul__int_r(self):
        result = self.a * 3
        self.assertEqual(result.n, 2)
        self.assertEqual(result.p, 5)

    def test___mul__int_l(self):
        result = 3 * self.a
        self.assertEqual(result, 12)

    def test___truediv__(self):
        result = self.a / self.b
        self.assertEqual(result.n, 3)
        self.assertEqual(result.p, 5)

    def test___truediv__int_r(self):
        result = self.a / 3
        self.assertEqual(result.n, 3)
        self.assertEqual(result.p, 5)

    def test___truediv__int_l(self):
        result = 3 / self.a
        self.assertEqual(result, 3 / 4)

    def test___floordiv__(self):
        result = self.a // self.b
        self.assertEqual(result.n, 1)
        self.assertEqual(result.p, 5)

    def test___floordiv__int_r(self):
        result = self.a // 3
        self.assertEqual(result.n, 1)
        self.assertEqual(result.p, 5)

    def test___floordiv__int_l(self):
        result = 3 // self.a
        self.assertEqual(result, 0)

    def test___mod__(self):
        result = self.a % self.b
        self.assertEqual(result.n, 1)
        self.assertEqual(result.p, 3)

    def test___mod__int_r(self):
        result = self.a % 3
        self.assertEqual(result.n, 1)
        self.assertEqual(result.p, 3)

    def test___mod__int_l(self):
        result = 3 % 4
        self.assertEqual(result, 3)

    def test___pow__(self):
        result = self.a ** self.b
        self.assertEqual(result.n, 4)
        self.assertEqual(result.p, 5)

    def test___pow__int_r(self):
        result = self.a ** 3
        self.assertEqual(result.n, 4)
        self.assertEqual(result.p, 5)

    def test___pow__int_l(self):
        result = 3 ** self.a
        self.assertEqual(result, 81)

    def test___neg__(self):
        result = -self.a
        self.assertEqual(result.n, 1)
        self.assertEqual(result.p, 5)

    def test___pos__(self):
        result = self.a
        self.assertEqual(result.n, 4)
        self.assertEqual(result.p, 5)

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
        self.assertEqual(type(int(self.a)), int)
        self.assertEqual(int(self.a), 4)
