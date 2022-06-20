import unittest
import re

def is_valid_IP(ip):
    for num in ip.split("."):
        if num.isdigit() and 0 <= int(num) <= 255:
            if num[0] == "0" and len(num) > 1:
                return False
            else:
                next
        else:
            return False
    return len(ip.split(".")) == 4

def is_valid_IP2(ip):
    return bool(re.match(r"^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])(\.(?!$)|$)){4}(?=$)", ip))

def is_valid_IP3(strng):
    lst = strng.split('.')
    passed = 0
    for sect in lst:
        if sect.isdigit():
            if sect[0] != '0':
                if 0 < int(sect) <= 255:
                    passed += 1
    return passed == 4

print(is_valid_IP('256.1.2.3'))
print(is_valid_IP('127.1.1.0'))
print(is_valid_IP('1.2.3.4.5'))
print(is_valid_IP('1.02.3.4'))

class Test(unittest.TestCase):

    def test1(self):
        self.assertEqual(is_valid_IP('12.255.56.1'),     True)

    def test2(self):
        self.assertEqual(is_valid_IP(''),                False)

    def test3(self):
        self.assertEqual(is_valid_IP('abc.def.ghi.jkl'), False)

    def test4(self):
        self.assertEqual(is_valid_IP('123.456.789.0'),   False)

    def test5(self):
        self.assertEqual(is_valid_IP('12.34.56'),        False)

    def test6(self):
        self.assertEqual(is_valid_IP('12.34.56 .1'),     False)

    def test7(self):
        self.assertEqual(is_valid_IP('12.34.56.-1'),     False)

    def test8(self):
        self.assertEqual(is_valid_IP('123.045.067.089'), False)

    def test9(self):
        self.assertEqual(is_valid_IP('127.1.1.0'),       True)

    def test10(self):
        self.assertEqual(is_valid_IP('0.0.0.0'),         True)

    def test11(self):
        self.assertEqual(is_valid_IP('0.34.82.53'),      True)

    def test12(self):
        self.assertEqual(is_valid_IP('192.168.1.300'),   False)

    def test13(self):
        self.assertEqual(is_valid_IP('256.1.2.3'),       False)

    def test14(self):
        self.assertEqual(is_valid_IP('123,45,67,89'),    False)
    
if __name__ == '__main__':
    unittest.main()