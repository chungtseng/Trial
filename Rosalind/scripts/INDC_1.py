def INDC(n):
    from scipy.misc import comb
    from math import log10
    prod = 2**(2*n)
    A = [-2*n*log10(2)]*2*n
    for i in xrange(2*n):
        prod -= comb(2*n, i,exact=True)
        print prod
        A[i] += log10(prod)
    return A

for i in INDC(42):
    print i,
        
