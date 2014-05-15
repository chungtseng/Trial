def ITWV(s,seqs):
    from itertools import product
    def sub_inds(s,u):
        from itertools import permutations
        perms = []
        for i in permutations(range(len(s)),len(u)):
            perms.append(i)
        perms_asc_ind = filter(lambda l: all([l[i+1] > l[i] for i in xrange(0,len(l) - 1)]), perms)
        perms_asc = {perm:[s[i] for i in perm] for perm in perms_asc_ind}
        results = []
        for i in perms_asc:
            if ''.join(perms_asc[i]) == u:
                results.append(i)
        return results
    def interwoven(pair):
        a = pair[0]
        b = pair[1]
        n = len(a) + len(b)
        start = min([min(a),min(b)])
        for i in xrange(start, start+n):
            if i not in a and i not in b:
                return False
        else:
            return True
    results = [[0 for i in xrange(len(seqs))] for j in xrange(len(seqs))]   
    for ii,i in enumerate(seqs):
        for ij,j in enumerate(seqs):
            a = sub_inds(s,i)
            b = sub_inds(s,j)
            c = product(a,b)
            for pair in c:
                if interwoven(pair):
                    results[ii][ij] = 1
                    break
    return results
if __name__ == '__main__':
    seqs=[]
    with open('/home/ycz/Rosalind/input/ITWV_in.txt', 'rb') as in_data:
        for line in in_data:
           seqs.append(line.strip())
    s = seqs[0]
    for i in ITWV(s,seqs[1:]):
        print ' '.join(i)
    
