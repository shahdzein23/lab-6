import unittest

class TestCalculator(unittest.TestCase):
    def test_add(self): self.assertEqual(Calculator().add(2, 3), 5)
