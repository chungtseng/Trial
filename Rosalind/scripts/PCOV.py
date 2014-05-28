def PCOV(seqs):
    n = len(seqs)
    k = len(seqs[0])
    s = seqs[0]
    while len(s) != n:
        for i in xrange(1,n):
            if s[-k+1:] == seqs[i][:-1]:
                #print s
                s += seqs[i][-1]
                break
    return s
        

if __name__ == '__main__':
    seqs = []
    with open('/home/ycz/Rosalind/input/PCOV_in.txt','rb') as in_data:
        for line in in_data:
            seqs.append(line.strip())
    print PCOV(seqs)
