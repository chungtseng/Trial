def ITWV(s,seqs):
    def check_interweave(dna1, dna2, superstr):
        if len(superstr) == 0:
            return True
        elif dna1[0] == dna2[0] == superstr[0]:
            return check_interweave(dna1[1:], dna2, superstr[1:]) or check_interweave(dna1, dna2[1:], superstr[1:])
        elif dna1[0] == superstr[0]:
            return check_interweave(dna1[1:], dna2, superstr[1:])
        elif dna2[0] == superstr[0]:
            return check_interweave(dna1, dna2[1:], superstr[1:])
        else:
            return False

    results = [[0 for i in xrange(len(seqs))] for j in xrange(len(seqs))]   
    for ii,i in enumerate(seqs):
        for ij,j in enumerate(seqs):
            for ind in xrange(0, len(s) - len(i) - len(j)):
                if check_interweave(i+'S',j+'S',s[ind:ind+len(i)+len(j)]):
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
        print ' '.join(map(str,i))
    
