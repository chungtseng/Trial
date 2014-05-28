def m(k,n):
    if k == 1:
        return 4
    return sum([m(k,n) for k in xrange(1,n+1)])
print m(5,9)
