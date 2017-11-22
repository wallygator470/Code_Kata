import unittest

"""  this was my version

import re

def order(sentence):
    words = sentence.split()
    i = 0
    for word in words:
        words[i] = re.search(r"\d", word).group() + word
        i += 1
    words.sort()
    j = 0
    for word in words:
        words[j] = word[1:]
        j += 1
    
    print(createSentence(words))
    return createSentence(words)

def createSentence(words):
    newSentence = ""
    for word in words:
        newSentence += word + " "
        
    return newSentence.strip()
    
the version I liked best is below"""

def extract_number(word):
    for l in word: 
        if l.isdigit(): return int(l)
    return None

def order(sentence):
    return ' '.join(sorted(sentence.split(), key=extract_number))

class Test(unittest.TestCase):
    
    def test_order(self):
        self.assertEqual(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")

if __name__ == '__main__':
    unittest.main()