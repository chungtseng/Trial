def QRT(taxa,c):
    result = []
    from itertools import combinations,product
    for i in c:
        if i.count('1') >= 2 and i.count('0') >= 2:
            ones = [ind for ind in xrange(len(i)) if i[ind] == '1']
            zeroes = [ind for ind in xrange(len(i)) if i[ind] == '0']
            one_comb = combinations(ones,2)
            zero_comb = combinations(zeroes,2)
            combs = product(one_comb,zero_comb)
            result.append([tuple([taxa[k] for k in comb[0]]) + tuple([taxa[j] for j in comb[1]]) for comb in combs]) 
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
    c = []
    with open('/home/ycz/Rosalind/input/QRT_in.txt','rb') as in_data:
        taxa = in_data.readline().strip().split(' ')
        for line in in_data:
            c.append(line.strip())
#    print taxa,c
    raw_results = QRT(taxa,c)
    results = []
    for i in raw_results:
        for j in i:
            for k in results:
                if equi(j,k):
                    break
            else:
                results.append(j)
    results = set(results)
    with open('/home/ycz/Rosalind/output/QRT_out.txt','w+') as out_data:
        for j in results:
            out_data.write('{%s, %s} {%s, %s}\n' % (j[0],j[1],j[2],j[3]))
