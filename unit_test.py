import unittest
from pick_1_in_array import *

class TestResult(unittest.TestCase):
    def test_result(self):
        self.assertAlmostEqual(find_unique_number([2,2,2,1]),1)
        self.assertAlmostEqual(find_unique_number([2,2,1,2]),1)
        self.assertAlmostEqual(find_unique_number([2,1,2,2]),1)
        self.assertAlmostEqual(find_unique_number([1,2,2,2]),1)

        self.assertAlmostEqual(find_unique_number([2,1,1,1]),2)
        self.assertAlmostEqual(find_unique_number([1,2,1,1]),2)
        self.assertAlmostEqual(find_unique_number([1,1,2,1]),2)
        self.assertAlmostEqual(find_unique_number([1,1,1,2]),2)

if __name__ == '__main__':
    unittest.main()