import unittest
import numpy as np
from FindMax import findMaxLinear, findMaxLinearWithCount, findMaxDNC, findMaxDNCWithCount, findSecondLinear

class MaxTest(unittest.TestCase):
  def setUp(self):
    self.short_list = np.array([7, 1, 2, 3, 4, 5, 10])
    l = np.random.randint(1, 100)
    self.random_list = np.random.randint(1, 100, l)

  def test_findMaxLinear_01(self):
    self.assertEqual(findMaxLinear(self.short_list), 10)

  def test_findMaxLinear_02(self):
    self.assertEqual(findMaxLinear(self.random_list), max(self.random_list))

  def test_findMaxLinearWithCount_01(self):
     self.assertSequenceEqual(findMaxLinearWithCount(self.short_list), (10, len(self.short_list) - 1))

  def test_findMaxLinearWithCount_02(self):
     actual = (findMaxLinear(self.random_list), len(self.random_list) - 1)
     result = findMaxLinearWithCount(self.random_list)
     self.assertSequenceEqual(result, actual)

  def test_findMaxDNC_01(self):
    self.assertEqual(findMaxDNC(self.short_list, 0, len(self.short_list) - 1), 10)

  def test_findMaxDNC_02(self):
    self.assertEqual(findMaxDNC(self.random_list, 0, len(self.random_list) - 1), max(self.random_list))

  def test_findMaxDNCWithCount_01(self):
     result = findMaxDNCWithCount(self.short_list, 0, len(self.short_list) - 1)
     self.assertSequenceEqual(result, (10, len(self.short_list) - 1))

  def test_findMaxDNCWithCount_02(self):
     actual = (findMaxLinear(self.random_list), len(self.random_list) - 1)
     result = findMaxDNCWithCount(self.random_list, 0, len(self.random_list) - 1)
     self.assertSequenceEqual(result, actual)

  def test_findSecondLinear_01(self):
    self.assertEqual(findSecondLinear(self.short_list), 7)

  def test_findSecondLinear_02(self):
    self.assertEqual(findSecondLinear(self.short_list[:-1]), 5)


if __name__ == '__main__': 
    unittest.main()