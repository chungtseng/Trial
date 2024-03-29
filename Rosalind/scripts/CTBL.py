def CTBL(newick):
    import re
    import operator
    results = []
    toks = re.split('([(),])',newick)
    #print toks
    leaves = {ind:node for ind,node in enumerate(toks) if re.match('[^();,]',node) and node != ''}
    leaves_set_1 = set([node for node in toks if re.match('[^();,]',node) and node != ''])
    leaves_set_2 = set([node for node in toks if re.match('[A-Z]',node)])
    print leaves_set_1 - leaves_set_2
    print len(leaves)
    #print leaves
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
    result = []
    from itertools import combinations,product
    for i in c:
        if i.count('1') >= 2 and i.count('0') >= 2:
            ones = [ind for ind in xrange(len(i)) if i[ind] == '1']
            zeroes = [ind for ind in xrange(len(i)) if i[ind] == '0']
            one_comb = combinations(ones,2)
            zero_comb = combinations(zeroes,2)
            combs = product(one_comb,zero_comb)
            result.append([tuple([k for k in comb[0]]) + tuple(j for j in comb[1]]) for comb in combs]) 
    return result
def equi(q1,q2):
    if q1 == q2:
        return True
    elif q1[0] in q2[2:] and q1[1] in q2[2:] and q1[2] in q2[0:2] and q1[3] in q2[0:2]:
        return True
    elif q1[0] in q2[0:2] and q1[1] in q2[0:2] and q1[2] in q2[2:] and q1[3] in q2[2:]:
        return True
    else:
        return False                    

if __name__ == '__main__':
    with open('/home/ycz/Rosalind/input/CTBL_in.txt', 'rb') as in_data:
        newick = in_data.readline().strip()
    m = CTBL(newick)
    c = []
    for i in m:
        c.append(''.join(map(str,i)))
    raw_results = QRT(c)
    results = []
    for i in raw_results:
        for j in i:
            for k in results:
                if equi(j,k):
                    break
            else:
                results.append(j)
    result = len(results)
    with open('/home/ycz/Rosalind/output/CTBL_out.txt','w+') as out_data:
        for i in m:
            out_data.write(''.join(map(str,i)))
            out_data.write('\n')
