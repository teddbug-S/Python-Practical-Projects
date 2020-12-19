import random
import unittest

from hangman_comps import word_list
from transposition_cipher import cipher_text, decipher_text


class TestTranspositionCipher(unittest.TestCase):
    """ A class to test the components of the transposition cipher code.

    :param TestCase: Inherits from unittest.TestCase
    :type TestCase: unittest
    """
    def test_cipher(self):
        """ Test for accurate cipher generations. """
        
        text = ' '.join(random.sample(word_list, random.randint(7, 70)))
        print(text)
        key = random.randint(len(text)//2, len(text))
        ciphered_text = cipher_text(text, key)
        self.assertEqual(decipher_text(ciphered_text, key), text)

    def test_cipher_1(self):
        """ Test for accurate cipher generations. """
        
        self.test_cipher()

    def test_cipher_2(self):
        """ Test for accurate cipher generations. """
        
        self.test_cipher()

    def test_cipher_3(self):
        """ Test for accurate cipher generations. """
        
        self.test_cipher()

    def test_cipher_4(self):
        """ Test for accurate cipher generations. """
        
        self.test_cipher()

    def test_cipher_5(self):
        """ Test for accurate cipher generations. """
        self.test_cipher()

    def test_cipher_6(self):
        """ Test for accurate cipher generations. """
        self.test_cipher()

    def test_cipher_7(self):
        """ Test for accurate cipher generations. """
        
        self.test_cipher()


if __name__ == '__main__':
    unittest.main()

