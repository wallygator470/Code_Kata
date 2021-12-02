import unittest

PINPAD = {
    "1": ["1", "2", "4"],
    "2": ["1", "2", "3", "5"],
    "3": ["2", "3", "6"],
    "4": ["1", "4", "5", "7"],
    "5": ["2", "4", "5", "6", "8"],
    "6": ["3", "5", "6", "9"],
    "7": ["4", "7", "8"],
    "8": ["0", "5", "7", "8", "9"],
    "9": ["6", "8", "9"],
    "0": ["0", "8"]
    }

def get_pins(observed):
    return getCombos([PINPAD[c] for c in observed])

def getCombos(ls):
    if len(ls) == 1:
        return ls[0]
    else:
        ans = []
        for s1 in getCombos(ls[1:]):
            for s2 in ls[0]:
                ans.append(s2+s1)
        return sorted(ans)

"""  this was my method
def get_pins(observed):

    digits = list(observed)
    possibleDigits = []

    for digit in digits:
        possibleDigits.append(PINPAD.get(digit))
    
    combos = []
    for i in range(len(possibleDigits)):
        if i == 0:
            combos = possibleDigits[i]
        else:
            curCombos = []
            for combo in combos:
                for digit in possibleDigits[i]:
                    curCombos.append(combo + digit)
            combos = curCombos

    print(combos)
    return sorted(combos)"""

print(get_pins("369"))

class Test(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(get_pins('8'), sorted(['5','7','8','9','0']))
    
    def test2(self):
        self.assertEqual(get_pins('11'), sorted(["11", "22", "44", "12", "21", "14", "41", "24", "42"]))
    
    def test3(self):
        self.assertEqual(get_pins('369'), sorted(["339","366","399","658","636","258","268","669","668","266","369","398","256","296","259","368","638","396","238","356","659","639","666","359","336","299","338","696","269","358","656","698","699","298","236","239"]))

if __name__ == '__main__':
    unittest.main()
    