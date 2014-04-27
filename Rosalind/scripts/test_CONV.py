import CONV
import unittest
import 063_NKEW
class testCONV(unittest.TestCase):
    def setUp(self):
        self.a,self.b = CONV.read_conv('/home/ycz/Rosalind/input/CONV_in.txt')
        self.assertTrue('\n' not in self.a[-1])
    def test2(self):
        self.assertTrue(type(CONV.CONV(self.a,self.b)) == tuple)
        self.assertTrue(type(CONV.CONV(self.a,self.b)[1]) == float)
    def test_truth(self):
        self.assertEqual(CONV.main(),063_NKEW.main())
if __name__ == '__main__':
    unittest.main()
