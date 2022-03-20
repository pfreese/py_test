import unittest
import swap_first_last

class TestFrontBack(unittest.TestCase):

    def test_length_0(self):
        self.assertEqual(swap_first_last.front_back(""), "")

    def test_length_1(self):
        self.assertEqual(swap_first_last.front_back("a"), "a")

    def test_length_2(self):
        self.assertEqual(swap_first_last.front_back("aQ"), "Qa")

    def test_length_geq_3(self):
        self.assertEqual(swap_first_last.front_back("ABCDE"), "EBCDA")
        self.assertEqual(swap_first_last.front_back("___"), "___")

if __name__ == '__main__':
    unittest.main()
