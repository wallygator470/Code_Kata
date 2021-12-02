#import unittest

CARDS = {
    "2": 13,
    "3": 12,
    "4": 11,
    "5": 10,
    "6": 9,
    "7": 8,
    "8": 7,
    "9": 6,
    "T": 5,
    "J": 4,
    "Q": 3,
    "K": 2,
    "A": 1 
    }

SUITSA = {
    "C": 1,
    "D": 2,
    "H": 3,
    "S": 4
    }

SUITS = [
    "C",
    "D",
    "H",
    "S"
    ]
    
POKERHAND_RANK = {
    "Royal Flush": 1,
    "Straight Flush": 2,
    "4 of a Kind": 3,
    "Full House": 4,
    "Flush": 5,
    "Straight": 6,
    "3 of a kind": 7,
    "2 Pairs": 8,
    "Pair": 9,
    "High Card": 10
    }

def compare_with(observed):
    return 1

def Pokerhand(hand):
    cards = hand.split()

    def _getHandName(cards):
        suitCounts = {suit:[card[1] for card in cards].count(suit) for suit in [card[1] for card in cards] if suit in SUITS}
        
        if  suitCounts == 5:
            name = "Flush"
        else:
            name = "Not Flush"
        return name
    
    name = _getHandName(cards)
    return name
#def determine_hand(hand):
    
        

print(Pokerhand("AS KS QS JS TS"))
"""
class Test(unittest.TestCase):
    
    royal_flush = "AS KS QS JS TS"
    strt_flush = "4H 5H 6H 7H 8H"
    four_high = "KD KH KS KC 5C"
    four_low = "7D 7S 7C 7H JC"
    full_high = "QH QD QS JS JH"
    full_low = "3S 3C 3H TC TS"
    flush_high = "2H 5H 8H 9H AH" 
    flush_low = "2H 3H 4H 6H 7H" 
    strt_high = "AC TC KS JD QH"
    strt_low = "5C 4C 6C 2D 3S"
    three_high = "KC KH KD 5S 4C"
    three_low = "5C 6H 7D 5S 5C"
    pair_high = "JC JD 9H 8C 9D"
    pair_low = "4C 5D 6C 5S 4H"
    high_cd_high = "3C 7D 2D JD QH"
    high_cd_low = "2S 8S 5S 7S 4H"
    
    def test1(self):
        self.assertEqual(compare_with(Pokerhand()), "Win")
    
    def test2(self):
        self.assertEqual(compare_with('11'), "Loss")
    
    def test3(self):
        self.assertEqual(compare_with('369'), "Tie")
if __name__ == '__main__':
    unittest.main()"""
    