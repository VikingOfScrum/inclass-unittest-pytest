from palindrome import palindrome
import unittest
#Simple unittest procedures
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

    def test_sentences(self):
        assert palindrome('evil live') is True
        assert palindrome('I did did I') is True
        assert palindrome('murder redrum') is True
        assert palindrome('not today ton') is False
        assert palindrome('happy birthday') is False

if __name__ == '__main__':
    unittest.main()