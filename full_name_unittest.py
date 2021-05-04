import unittest
import full_name

class full_name_testing(unittest.TestCase):
    def test_name_pass(self):
        result = full_name.name("Andrew", "Kassab")
        self.assertEqual(result,"Andrew Kassab")

    def test_name_fail(self):
        result = full_name.name("Andrew", "Kassab")
        self.assertEqual(result,"AndrewKassab")

    def test_name_fail_2(self):
        result = full_name.name("Andrew", "Kassab")
        self.assertEqual(result,"Andrew kassab")
