import unittest

class Stack_tests(unittest.TestCase):

  def test_sum1(self):
    self.assertEqual(2 + 2, 4)
    self.assertEqual(2 + 2, 4)

  def test_sum2(self):
    self.assertEqual(12 + 24, 36)

  def test_logic1(self):
    self.assertTrue(12 < 24)

  def test_logic2(self):
    self.assertFalse("word" == "WORD")

  def test_float(self):
    # falla por un problema de aproximación en punto flotante
    self.assertEqual(0.1 + 0.2, 0.3)

if __name__ == "__main__":
  unittest.main()
