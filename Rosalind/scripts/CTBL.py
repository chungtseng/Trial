def CTBL(newick):
    import re
    import operator
    results = []
    toks = re.split('([(),])',newick)
    print toks
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
                    

if __name__ == '__main__':
    with open('/home/ycz/Rosalind/input/CTBL_in.txt', 'rb') as in_data:
        newick = in_data.readline().strip()
    m = CTBL(newick)
    with open('/home/ycz/Rosalind/output/CTBL_out.txt','w+') as out_data:
        for i in m:
            out_data.write(''.join(map(str,i)))
            out_data.write('\n')
