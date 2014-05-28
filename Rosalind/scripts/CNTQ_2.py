def CTBL(newick):
    import re
    import operator
    results = []
    toks = re.split('([(),])',newick)
    leaves = {ind:node for ind,node in enumerate(toks) if re.match('[^();,]',node) and node != ''}
    pn = 2
    pi = 0
    for ind,tok in enumerate(toks):
        if tok == '(':
            pi += 1
        if pi == pn:
            pn += 1
            p_1 = 1
            p_2 = 0
            start = ind
            for rind,rtok in enumerate(toks[ind+1:]):
                if rtok == ')':
                    p_2 += 1
                elif rtok == '(':
                    p_1 += 1
                
                if p_1 == p_2:
                    end = ind + rind + 1
                    break
            rec = {}
            for i in leaves:
                if i > start and i < end:
                    rec[leaves[i]] = 0
                else:
                    rec[leaves[i]] = 1
            sorted_rec = sorted(rec.iteritems(), key=operator.itemgetter(0))
            results.append([i[1] for i in sorted_rec])
    return results
def QRT(c):
    result = 0
    from scipy.misc import comb
    for i in c:
        ones = i.count('1')
        zeroes = i.count('0')
        one_comb = comb(ones,2,exact=True)
        zero_comb = comb(zeroes,2,exact=True)
        combs = one_comb * zero_comb
        result += combs
        result = result % 10**6
    return result

if __name__ == '__main__':
    with open('/home/ycz/Rosalind/input/CNTQ_in2.txt', 'rb') as in_data:
        n = int(in_data.readline().strip())
        newick = in_data.readline().strip()
    m = CTBL(newick)
    #print m
    c = []
    for i in m:
        c.append(''.join(map(str,i)))
    raw_results = QRT(c)
    print raw_results - n


