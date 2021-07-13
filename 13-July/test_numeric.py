import unittest

import numeric

class TestAdd(unittest.TestCase):
    def test_regular(self):
        self.assertEqual(numeric.add(4,5), 9)

    def test_with_zero(self):
        self.assertEqual(numeric.add(4,0), 4)

class TestDiv(unittest.TestCase):
    def test_regular(self):
        self.assertEqual(numeric.div(5,2), 2.5)


if __name__ == "__main__":
    unittest.main()
