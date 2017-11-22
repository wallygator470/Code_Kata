import unittest

def domain_name(url):
    print(url)
    print(url.split("//")[-1].split("www.")[-1].split(".")[0])
    return url.split("//")[-1].split("www.")[-1].split(".")[0]

class Test(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(domain_name("http://github.com/carbonfive/raygun"), "github")
    
    def test2(self):
        self.assertEqual(domain_name("http://www.zombie-bites.com"), "zombie-bites")
    
    def test3(self):
        self.assertEqual(domain_name("https://www.cnet.com"), "cnet")
    
    def test4(self):
        self.assertEqual(domain_name("www.xakep.ru"), "xakep")

if __name__ == '__main__':
    unittest.main()
