def CTBL(newick,seq):
    import re
    import operator
    results = []
    toks = re.split('([(),])',newick)
    leaves = {ind:node for ind,node in enumerate(toks) if re.match('[^();,]',node) and node != ''}
    leaves_set_1 = set([node for node in toks if re.match('[^();,]',node) and node != ''])
    leaves_set_2 = set([node for node in toks if re.match('[A-Z]',node)])
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
            sorted_rec = {}
            #print rec
            for i in seq:
                sorted_rec[i] = rec[i]
            results.append([i for i in sorted_rec.values()])
            
    return results
def shared_split_number(m,n):
    result = 0
    for i in m:
        if i in n:
            result += 1
    return result

if __name__ == '__main__':
    with open('/home/ycz/Rosalind/input/SPTD_in.txt', 'rb') as in_data:
        seq = in_data.readline().strip().split(' ')
        newick_1 = in_data.readline().strip()
        newick_2 = in_data.readline().strip()
    m = CTBL(newick_1,seq)
    n = CTBL(newick_2,seq)
    print 2*(len(seq)-3)-2*shared_split_number(m,n)
