def wfmd(n,m,g,k):
    from scipy.misc import comb
    p = float(m)/float(2*n)
    l = lambda lk: [1-sum([lk[i] for i in xrange(k)]) for k in xrange(2*n+1)]
    lk = lambda p,pp:[comb(2*n,kk,exact = True)*p**(2*n-kk)*(1-p)**kk*pp for kk in xrange(2*n+1)]
    sep_l = lk(p,1)
    if g == 1:
        return l[k]
    def nx_gr_sep(sep_l):
        result = [0] * (len(sep_l))
        for ind,ite in enumerate(sep_l):
            p = float((len(sep_l)-1-ind))/float(len(sep_l)-1)
            tmp_sep = lk(p,ite)
            for i in xrange(len(result)):
                result[i] += tmp_sep[i]
        return result
    for i in xrange(1,g):
        sep_l = nx_gr_sep(sep_l)
        print len(sep_l)
    print len(sep_l)
    return l(sep_l)[k]

print wfmd(5,9,5,5)
