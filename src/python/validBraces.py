import unittest

def validBraces(string):
    while True:
        newString = string
        string = string.replace('()', '')
        string = string.replace('{}', '')
        string = string.replace('[]', '')
        if newString == string:
            print(string, False)
            return False
        elif len(string) == 0:
            print(True)
            return True

def validBracesRecursive(string):
    braces = {"(" : ")", "[" : "]", "{" : "}"}
    newWord = []
    brace = string[0]
    if len(string) %2 != 0:
        print(string, False)
        return False
    elif brace in braces.values():
        print(string, False)
        return False
    elif len(string) == 0:
        print(True)
        return True
    else:
        l = len(string)
        for i in range(l):
            if braces[brace] == string[i] and (i - 1) % 2 == 0 and l > 2:
                newWord += string[i + 1:]
                return validBraces("".join(newWord))
            elif i == l - 1 and braces[brace] == string[i]:
                print(True)
                return True
            elif i == l - 1 and braces[brace] != string[i]:
                print(string, False)
                return False
            elif i == 0:
                next
            elif l == 2 and i == l:
                next
            else:
                newWord += string[i]

validBraces( "()" )
validBraces( "({[]}[])[]" )
validBraces( "(}" )
validBraces( "([)]" )
validBraces( "][" )
validBraces( "(][)" )
validBraces( "(){}[]" )
validBracesRecursive( "()" )
validBracesRecursive( "({[]}[])[]" )
validBracesRecursive( "(}" )
validBracesRecursive( "([)]" )
validBracesRecursive( "][" )
validBracesRecursive( "(][)" )
validBracesRecursive( "(){}[]" )

class Test(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(validBraces( "()" ), True)
    
    def test2(self):
        self.assertEqual(validBraces( "([)]" ), False)
    
    def test3(self):
        self.assertEqual(validBraces( "(){}[]" ), True)
    
    def test4(self):
        self.assertEqual(validBraces( "([{}])" ), True)
    
    def test5(self):
        self.assertEqual(validBraces( "(}" ), False)
    
    def test6(self):
        self.assertEqual(validBraces( "[(])" ), False)
    
    def test7(self):
        self.assertEqual(validBraces( "[({})](]" ), False)
    
    def test8(self):
        self.assertEqual(validBracesRecursive( "()" ), True)
    
    def test9(self):
        self.assertEqual(validBracesRecursive( "([)]" ), False)
    
    def test10(self):
        self.assertEqual(validBracesRecursive( "(){}[]" ), True)
    
    def test11(self):
        self.assertEqual(validBracesRecursive( "([{}])" ), True)
    
    def test12(self):
        self.assertEqual(validBracesRecursive( "(}" ), False)
    
    def test13(self):
        self.assertEqual(validBracesRecursive( "[(])" ), False)
    
    def test14(self):
        self.assertEqual(validBracesRecursive( "[({})](]" ), False)

if __name__ == '__main__':
    unittest.main()