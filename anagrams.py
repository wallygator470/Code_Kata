import unittest

def anagrams(word, words):
    return [wrd for wrd in words if sorted(wrd) == sorted(word)]

class Test(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
    
    def test2(self):
        self.assertEqual(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])
    
if __name__ == '__main__':
    unittest.main()