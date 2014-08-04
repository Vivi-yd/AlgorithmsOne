from math import ceil
from random import randrange

def split(x, m):
    """
    returns a tuple of quotient and remainder of x as divided
    by 10**m
    """
    return x // 10**m , x % 10**m


def karatsuba(x, y):
    """
    implements karatsuba algorithm for multiplying two numbers
    """
    #base case
    if x < 10 or y < 10:
        return x*y
    
    #get value of m (base 10)
    n = max(len(str(x)), len(str(y)))
    m = int(ceil(n/2.0))
    
    #get parts of input numbers
    x1, x0 = split(x, m)
    y1, y0 = split(y, m)
    
    #get three parts by recursion
    z2 = karatsuba(x1, y1)
    z0 = karatsuba(x0, y0)
    z1 = karatsuba(x1 + x0, y1 + y0) - z2 - z0
    
    ans = z2 * 10**(2*m)  +  z1 * 10**m  +  z0
    return ans
    
def test_karatsuba():
	"""
	test by picking random numbers
	"""
    failed = 0
    for i in range(200): 
        x = randrange(100, 1000000)
        y = randrange(100, 1000000)
        if karatsuba(x, y) != x*y:
            failed += 1

    if failed > 0:
        print "test fails for " + str(failed) + " number of cases"
    else:
        print "test passed"
        
test_karatsuba()


