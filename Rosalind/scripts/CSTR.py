def CSTR(seqs):
    results = []
    n = len(seqs[0])
    for i in xrange(n):
        tmp = [s[i] for s in seqs]
        schr = [0 if i == tmp[0] else 1 for i in tmp]
        if sum(schr) > 1 and sum(schr) < len(seqs)-1:
            results.append(schr)
    return results

if __name__ == '__main__':
    seqs = []
    with open('/home/ycz/Rosalind/input/CSTR_in.txt','rb') as in_data:
        for line in in_data:
            seqs.append(line.strip())
    a = CSTR(seqs)
    for i in a:
        print ''.join(map(str,i))
