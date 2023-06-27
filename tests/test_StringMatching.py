import unittest
from func_string_matching import StringMatching

class StringMatchingTest(unittest.TestCase):
    def test_StringMatching(self):
        string1 = "hello"
        string2 = "hallo"
        expected_similarity = 0.8
        self.assertAlmostEqual(StringMatching(string1, string2), expected_similarity, places=2)

    def test_StringMatching_case_insensitive(self):
        string1 = "HELLO"
        string2 = "hello"
        expected_similarity = 1.0
        self.assertAlmostEqual(StringMatching(string1, string2), expected_similarity, places=2)

if __name__ == '__main__':
    unittest.main()
