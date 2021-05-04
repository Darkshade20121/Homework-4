import unittest
import average

class average_test(unittest.TestCase):
    def test_average_pass(self):
        result = average.average_list(list = [1,2,3,4,5])
        self.assertEqual(result,3.0)

    def test_average_pass_2(self):
        result = average.average_list(list = [5,6,7,8,9])
        self.assertEqual(result,7.0)

    def test_average_fail(self):
        result = average.average_list(list = [1,2,3,4,100,5000])
        self.assertEqual(result,5)
