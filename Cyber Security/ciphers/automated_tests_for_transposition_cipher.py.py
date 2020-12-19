import random
from textwrap import fill

from transposition_cipher import cipher_text, decipher_text
from hangman_comps import word_list


class TestCipher:
    
    def __init__(self) -> None:
        self.word_list = word_list


    def generate_sentence(self):
        sentence_len = random.randint(7, 40)
        sample_words = random.sample(self.word_list, sentence_len)
        sentence = ' '.join(sample_words)
        return sentence

    
    def generate_key(self, sentence_len):
        """ Generates a key

        :param sentence_len: length of the plain text
        :type sentence_len: int
        :return: key
        :rtype: int
        """
        key = random.randint((sentence_len//2)//2, sentence_len - sentence_len//2+random.randint(2, 8))
        return key

    
    def run_tests(self, no_of_tests=50, verbose=False):
        """ 
        Run the tests

        :param no_of_tests: number of tests to run, defaults to 50
        :type no_of_tests: int, optional
        """
        print(f"\n\t🔰🔰🔰🔰🔰🔰🔰{f' TESTING {no_of_tests} CASES. '}🔰🔰🔰🔰🔰🔰🔰\n".expandtabs(40))
        for n in range(1, no_of_tests+1):
            sentence = self.generate_sentence()
            key = self.generate_key(len(sentence))
            print(f"Test No.{n}🔰:")
            if verbose:
                print(f"""   |Sentence:\n\t|'''{fill(sentence, 40, subsequent_indent='        |')}''' """)
                print(f"   |Key:\n\t|{key}| ")
            ciphered_text = cipher_text(sentence, key)
            deciphered_text = decipher_text(ciphered_text, key)
            try:
                assert sentence == deciphered_text
            except AssertionError:
                print(f"\n  |Test number {n} failed.❌❌\n")
            else:
                print("\n   |Passed. ✅✅\n")



if __name__ == '__main__':
    tester = TestCipher()
    tester.run_tests(verbose=True)


