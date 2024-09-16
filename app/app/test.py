"""
    This is a test file
"""
from django.test import SimpleTestCase

from app import calc


class TestCalc(SimpleTestCase):
    """Test the calc moduke"""

    def test_add(self):
        """Test the add function"""
        self.assertEqual(calc.add(3, 8), 11)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        """Test the subtract function"""
        self.assertEqual(calc.subtract(5, 11), -6)
        self.assertEqual(calc.subtract(1, 1), 0)
        self.assertEqual(calc.subtract(-1, 1), -2)
