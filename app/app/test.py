"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add(self):
        res = calc.add(10, 11)

        self.assertEqual(res, 21)

    def test_substact(self):
        res = calc.substract(15, 10)

        self.assertEqual(res, 5)