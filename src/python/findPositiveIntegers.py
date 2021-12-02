def findPositiveIntegers(n, p):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            for c in range(1, n + 1):
                for d in range(1, n + 1):
                    if pow(a, p) + pow(b, p) == pow(c, p) + pow(d, p):
                        print(a, b, c, d)

def findPositiveIntegersRoot(n, p):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            for c in range(1, n + 1):
                d = int(round(abs((a ** p) + (b ** p) - (c ** p)) ** (1. / p)))
                if (a ** p) + (b ** p) == (c ** p) + (d ** p) and d <= n:
                    print(a, b, c, int(d)) 

findPositiveIntegers(10, 3)
findPositiveIntegersRoot(10, 3)
