import unittest
import TRIE
class testTRIE(unittest.TestCase):
    def test_read_input(self):
        self.dna = TRIE.read_input('/home/ycz/Rosalind/input/TRIE_in.txt')
        f = open('/home/ycz/Rosalind/input/TRIE_in.txt', 'rb')
        ln = ''.join(f.readlines()).count('\n')
        self.assertTrue(type(self.dna) == list)
        self.assertEqual(len(self.dna), ln)
        self.assertTrue(self.dna[-1] not in '\n\r')

if __name__ == '__main__':
    unittest.main()
