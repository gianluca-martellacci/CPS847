import unittest
from add import add

class TestAdder(unittest.TestCase):

	def	test_pos(self):
		self.assertEqual(10, add(9, 1))

	def test_neg(self):
		self.assertEqual(0, add(2, -2))

