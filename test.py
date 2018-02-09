import unittest
from compress import compress


class KataTestCase(unittest.TestCase):

    def test_input_a_returns_a(self):
        expected = "a"
        received = compress("a")
        self.assertEqual(expected, received)

    def test_input_b_returns_b(self):
        expected = "b"
        received = compress("b")
        self.assertEqual(expected, received)

    def test_input_ab_returns_ab(self):
        expected = "ab"
        received = compress("ab")
        self.assertEqual(expected, received)

    def test_input_aab_returns_a2b(self):
        expected = "a2b"
        received = compress("aab")
        self.assertEqual(expected, received)

    def test_input_aaabbbbc_returns_a3b4c(self):
        expected = "a3b4c"
        received = compress("aaabbbbc")
        self.assertEqual(expected, received)

    def test_input_bbbaaabbbbc_returns_a3b4c(self):
        expected = "b3a3b4c"
        received = compress("bbbaaabbbbc")
        self.assertEqual(expected, received)


if __name__ == '__main__':
    unittest.main()
