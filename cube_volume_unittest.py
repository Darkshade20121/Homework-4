import unittest
import cube_volume

class volume_test(unittest.TestCase):
    def test_volume_pass(self):
        result = cube_volume.cube(10)
        self.assertEqual(result,1000)
    
    def test_volume_pass_2(self):
        result = cube_volume.cube(5)
        self.assertEqual(result,125)

    def test_volume_fail(self):
        result = cube_volume.cube(1)
        self.assertEqual(result,4)



