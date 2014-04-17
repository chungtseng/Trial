def EDTA(sequence_1,sequence_2):
    n = len(sequence_1)
    m = len(sequence_2)
    score_mat = [[float('Infinity') for i in range(m+1)] for j in range(n+1)]
    track_mat = [[ 0 for i in range(m+1)] for j in range(n+1)]
    for i in range(n+1):
        score_mat[i][0] = i
    for i in range(m+1):
        score_mat[0][i] = i
    for row in range(n):
        for col in range(m):
            left = score_mat[row+1][col] + 1
            up = score_mat[row][col+1] + 1
            if sequence_1[row] == sequence_2[col]:
                    upper_left = score_mat[row][col]
            else:
                    upper_left = score_mat[row][col] + 1
            score = [upper_left,left,up]
            track = ['upper_left','left','up']
            for i in range(3):
                    if score[i] < score_mat[row+1][col+1]:
                            score_mat[row+1][col+1] = score[i]
                            track_mat[row+1][col+1] = track[i]
    
    row,col = n,m
    seq_1,seq_2 = '',''
    while row != 0 and col != 0:
                if track_mat[row][col] == 'upper_left':
                        seq_1 = sequence_1[row-1] + seq_1
                        seq_2 = sequence_2[col-1] + seq_2
                        row -= 1
                        col -= 1
                elif track_mat[row][col] == 'left':
                        seq_1 = '-'  + seq_1
                        seq_2 = sequence_2[col-1] + seq_2
                        col -= 1
                elif track_mat[row][col] == 'up':
                        seq_1 = sequence_1[row-1] + seq_1
                        seq_2 = '-' + seq_2
                        row -= 1
    return score_mat[n][m],seq_1,seq_2



if __name__ == '__main__':
    from FASTA import FASTA
    fasta = FASTA('/home/ycz/Rosalind/input/EDTA.txt')
    seqs = fasta.sequences()
    result = EDTA(seqs[0],seqs[1])
    print seqs
    print(result)
    with open('/home/ycz/Rosalind/output/EDTA_out.txt','w+') as output:
        output.write('\n'.join(map(str,result)))
