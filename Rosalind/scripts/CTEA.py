def CTEA(seqs):
    pr1 = seqs[0]
    pr2 = seqs[1]
    modulus = 2**27 - 1
    count = [[0 for i in xrange(len(pr2)+1)] for j in xrange(len(pr1)+1)]
    score = [[0 for i in xrange(len(pr2)+1)] for j in xrange(len(pr1)+1)]
    for i in xrange(len(pr1)+1):
        score[i][0] = i
        count[i][0] = 1
    for i in xrange(len(pr2)+1):
        score[0][i] = i
        count[0][i] = 1
    for i in xrange(1,len(pr2)+1):
        for j in xrange(1,len(pr1)+1):
            score_tmp = [score[j-1][i] + 1, score[j][i-1] + 1, score[j-1][i-1] if pr1[j-1] == pr2[i-1] else score[j-1][i-1] + 1]
            min_ind, min_score = min(enumerate(score_tmp), key=lambda p:p[1])
            
#            print min_score
            score[j][i] = min_score
            if score_tmp[0] == min_score:
                count[j][i] += count[j-1][i]
            if score_tmp[1] == min_score:
                count[j][i] += count[j][i-1]
            if score_tmp[2] == min_score:
                count[j][i] += count[j-1][i-1]
#    print count
    return count[len(pr1)][len(pr2)] % modulus
            
            
                
    

if __name__ == '__main__':
    from FASTA import FASTA
    fasta = FASTA('/home/ycz/Rosalind/input/CTEA_in.txt')
    seqs = fasta.sequences()
    #print seqs
    #print(result)
    #with open('/home/ycz/Rosalind/output/CTEA_out.txt','w+') as output:
    #    output.write('\n'.join(map(str,result)))
    print CTEA(seqs)
