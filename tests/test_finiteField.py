from unittest import TestCase
from objects.FiniteField import FiniteField
from objects.PolynomialModP import PolynomialModP


class TestFiniteField(TestCase):
    @classmethod
    def setUpClass(cls):
        p = PolynomialModP([1, 0, 1], 3)
        cls.F = FiniteField(p, 3)

    def test_additionTable(self):
        table = self.F.additionTable()
        print("\nAddition table: \n" + str(table))

    def test_multiplicationTable(self):
        table = self.F.multiplicationTable()
        print("\nMultiplication table: \n" + str(table))

    def test_elements(self):
        elements_expected = [[0], [1], [1, 0], [1, 1]]
        elements_result = self.F.elements()
        self.assertTrue(all([e in elements_result for e in elements_expected]))

    def test_primitiveElement(self):
        expected = PolynomialModP([0, 1, 1], 3)
        self.assertEqual(self.F.primitiveElement(), expected)

    def test_isIrreducible(self):
        pass
