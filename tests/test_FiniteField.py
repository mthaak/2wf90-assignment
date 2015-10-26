from unittest import TestCase
from objects.FiniteField import FiniteField
from objects.IntegerModP import IntegerModP
from objects.PolynomialModP import PolynomialModP


class TestFiniteField(TestCase):
    @classmethod
    def setUpClass(cls):
        p = PolynomialModP([1, 0, 1], 3)
        cls.F = FiniteField(p, 3)
        cls.a = [1, 1]
        cls.b = [2]

    def test___init__(self):
        F = FiniteField(PolynomialModP([1, 1], 5), 3)
        self.assertEqual(F.f, PolynomialModP([1, 1], 3))

    def test___init__list_f(self):
        F = FiniteField([1, 1], 3)
        self.assertEqual(F.f, PolynomialModP([1, 1], 3))

    def test___init__notpolynomial_f(self):
        with self.assertRaises(ValueError):
            FiniteField("string", 3)

    def test___init__notinteger_p(self):
        with self.assertRaises(ValueError):
            FiniteField([1, 1], 2.5)

    def test___init__notprime_p(self):
        with self.assertRaises(ValueError):
            FiniteField([1, 1], 12)

    def test___init__toosmall_p(self):
        with self.assertRaises(ValueError):
            FiniteField([1, 1], 1)

    def test___init__toolarge_p(self):
        with self.assertRaises(ValueError):
            FiniteField([1, 1], 101)

    def test___init__notirreducible_f(self):
        with self.assertRaises(ValueError):
            FiniteField([1, 0, 1], 2)

    def test___init__constant_f(self):
        with self.assertRaises(ValueError):
            FiniteField(PolynomialModP([1], 3), 3)

    def test_additionTable(self):
        print("\nAddition table:")
        self.F.additionTable()

    def test_multiplicationTable(self):
        print("\nMultiplication table:")
        self.F.multiplicationTable()

    def test_elements(self):
        elements_expected = [[0], [1], [1, 0], [1, 1]]
        elements_result = self.F.elements()
        self.assertTrue(all([e in elements_result for e in elements_expected]))

    def test_isPrimitive_polynomial(self):
        self.assertTrue(self.F.isPrimitive(PolynomialModP([1, 0], 5)))

    def test_isPrimitive_list(self):
        self.assertTrue(self.F.isPrimitive([1, 0]))

    def test_isPrimitive_other(self):
        with self.assertRaises(ValueError):
            self.F.isPrimitive("string")

    def test_primitiveElement(self):
        expected = PolynomialModP([1, 0], 3)
        self.assertEqual(self.F.primitiveElement(), expected)

    def test_isIrreducible_polynomial(self):
        self.assertTrue(self.F.isIrreducible(PolynomialModP([1, 0, 1], 5)))

    def test_isIrreducible_list(self):
        self.assertTrue(self.F.isIrreducible([1, 0, 1]))

    def test_isIrreducible_other(self):
        with self.assertRaises(ValueError):
            self.F.isIrreducible("string")

    def test_isIrreducible_toosmall_0(self):
        with self.assertRaises(ValueError):
            self.F.isIrreducible(PolynomialModP([1], 3))

    def test_isIrreducible_toosmall_1(self):
        with self.assertRaises(ValueError):
            self.F.isIrreducible(PolynomialModP([1, 1], 3))

    def test_irreducibleElement(self):
        self.assertEqual(self.F.irreducibleElement(2), PolynomialModP([1, 0, 1], 3))

    def test_irreducibleElement_toosmall_error(self):
        with self.assertRaises(ValueError):
            self.F.irreducibleElement(0)

    def test_irreducibleElement_notint_error(self):
        with self.assertRaises(ValueError):
            self.F.irreducibleElement(4.5)

    def test_sum_list(self):
        expected = PolynomialModP([1, 0], 3)
        self.assertEqual(self.F.sum(self.a, self.b), expected)
        self.assertEqual(self.F.sum(self.a + self.F.f * 2, self.b + self.F.f * 7), expected)

    def test_sum_poly(self):
        expected = PolynomialModP([1, 0], 3)
        self.assertEqual(self.F.sum(PolynomialModP(self.a, 5), PolynomialModP(self.b, 7)), expected)

    def test_sum_other_l(self):
        with self.assertRaises(ValueError):
            self.F.sum("string", PolynomialModP(self.a, 5), )

    def test_sum_other_r(self):
        with self.assertRaises(ValueError):
            self.F.sum(PolynomialModP(self.a, 5), "string")

    def test_product_list(self):
        expected = PolynomialModP([2, 2], 3)
        self.assertEqual(self.F.product(self.a, self.b), expected)
        self.assertEqual(self.F.product(self.a + self.F.f * 3, self.b + self.F.f * 6), expected)

    def test_product_poly(self):
        expected = PolynomialModP([2, 2], 3)
        self.assertEqual(self.F.product(PolynomialModP(self.a, 5), PolynomialModP(self.b, 7)), expected)

    def test_quotient_list(self):
        expected = PolynomialModP([2, 2], 3)
        self.assertEqual(self.F.quotient(self.a, self.b), expected)
        # self.assertEqual(self.F.quotient(self.a + self.F.f * 4, self.b + self.F.f * 5), expected)

    def test_quotient_poly(self):
        expected = PolynomialModP([2, 2], 3)
        self.assertEqual(self.F.quotient(PolynomialModP(self.a, 5), PolynomialModP(self.b, 7)), expected)

    def test_exp_basis(self):
        expected = PolynomialModP([2, 1], 3)
        self.assertEqual(self.F.exp_basis(PolynomialModP([1, 1], 3), 3), expected)

    def test_3_6a(self):
        F = FiniteField(PolynomialModP([1, 0, 0, 1, 1], 2), 2)
        self.assertTrue(F.isIrreducible(PolynomialModP([1, 0, 0, 1, 1], 2)))

    def test_3_7(self):
        F = FiniteField(PolynomialModP([1, 0, -2], 5), 5)
        self.assertTrue(F.isIrreducible(PolynomialModP([1, 0, -2], 5)))

    # Exercise incorrect
    # def test_3_10(self):
    #     F = FiniteField(PolynomialModP([1, 0, 0, 0, 1, 1], 2), 2)
    #     self.assertTrue(F.isIrreducible(PolynomialModP([1, 0, 0, 0, 1, 1], 2)))

    def test_3_11(self):
        F = FiniteField(PolynomialModP([1, 0, 1, 1], 2), 2)
        self.assertEquals(F.primitiveElement(), PolynomialModP([1, 0], 2))

    def test_4_1(self):
        F = FiniteField(PolynomialModP([1, 1, 2, 1], 3), 3)
        self.assertFalse(F.isIrreducible(PolynomialModP([1, 0, 0, 1], 3)))

    def test_5_6(self):
        F = FiniteField(PolynomialModP([1, 1, 1, 1, 1], 2), 2)
        self.assertTrue(F.isIrreducible(PolynomialModP([1, 1, 1, 1, 1], 2)))
