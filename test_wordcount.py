from wordcount import wordsInString
import unittest
#Simple unittest procedures
wis = wordsInString
class testWordCount(unittest.TestCase):
    def test_true_counts(self):
        self.assertEqual(wis('hello world'), 2)
        self.assertEqual(wis('Today is going to be the day'), 7)
        self.assertEqual(wis('it is very nice outside'), 5)
        self.assertEqual(wis('Sometimes I wonder'), 3)

    def test_false_counts(self):
        self.assertNotEqual(wis("The red clown wore red shoes"), 4)
        self.assertNotEqual(wis("How do we reach these kids"), 5)
        self.assertNotEqual(wis("a dog once barked"), 3)
        self.assertNotEqual(wis("Its time for a nap I think"), 16)

if __name__ =='__main__':
    unittest.main()