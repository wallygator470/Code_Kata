import unittest

def unique_in_order(i):
    return [i[a] for a in range(len(i)) if i[a] != i[a-1] or a == 0]

class Test(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(unique_in_order('AAAABBBCCDAABBB'), ['A','B','C','D','A','B'])
    
if __name__ == '__main__':
    unittest.main()