from palindrome import palindrome
import unittest

class testPalindrome(unittest.TestCase):
    def test_true_statements(self):
        assert palindrome('uWu') is True
        assert palindrome('dad') is True
        assert palindrome('mom') is True
        assert palindrome('SAIPPUAKIVIKAUPPIAS') is True


    def test_false_statements(self):
        assert palindrome('dockers') is False
        assert palindrome('choice') is False
        assert palindrome('doggo') is False
        assert palindrome('mississippi') is False

if __name__ == '__main__':
    unittest.main()