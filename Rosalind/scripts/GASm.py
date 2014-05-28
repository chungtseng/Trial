def rc(s):
    bound = dict(zip('ATCG','TAGC'))
    result = ''
    for i in s:
        result = bound[i] + result
    return result

def GASM(seqs):
    from copy import deepcopy
    n = len(seqs)
    k = len(seqs[0])
    s = seqs[0]
    contained = {s:[]}
    frontier = [s]
    while frontier != []:
        print 'round'
        print frontier
        next_seqs = []
        for j in frontier:
            for i in xrange(1,n):
                for m in xrange(0,k):
                    print m,len(j),len(seqs[i])
                    if j[-k+m:] == seqs[i][:-m] and seqs[i] not in contained[j]:
                        
                        tmp = j + seqs[i][-m:]
                        print seqs[i]
                        contained[tmp] = contained[j].append(seqs[i])
                        next_seqs.append(tmp)
        frontier = deepcopy(next_seqs)
    
    return min([(i,contained[i]) for i in contained if len(contained[i]) == n/2],key=lambda x: len(x[0]))

if __name__ == '__main__':
    seqs = []
    with open('/home/ycz/Rosalind/input/GASM_in.txt', 'rb') as in_data:
        for line in in_data:
            seqs.append(line.strip())
    seqs_rc = map(rc,seqs)
    seqs_t = seqs + seqs_rc
    print GASM(seqs_t)
