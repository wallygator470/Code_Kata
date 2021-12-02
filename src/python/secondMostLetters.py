import unittest
"""
def secondMost(letters):
    return [letter[0] for letter in sorted({letter:letters.count(letter) for letter in letters}.items(), key = lambda item: item[1], reverse=True)][1]
"""

def secondMost(letters):
    counts = {letter:letters.count(letter) for letter in letters}
    letter = sorted(((counts[ltr], ltr) for ltr in counts), reverse=True)[1][1]
    print(letters)
    print(letter)
    return letter


class Test(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(secondMost(['a', 'b', 'c', 'b' ,'c', 'd', 'd', 'c', 'd', 'd']), 'c')
    
    def test2(self):
        self.assertEqual(secondMost(['a', 'b', 'c', 'b' ,'b', 'd', 'd', 'c', 'd', 'd']), 'b')
    
if __name__ == '__main__':
    unittest.main()