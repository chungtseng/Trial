def EDTA(sequence_1,sequence_2):
    n = len(sequence_1)
    m = len(sequence_2)
    score_mat = [[float('Infinity') for i in range(m+1)] for j in range(n+1)]
    track_mat = [[ 0 for i in range(m+1)] for j in range(n+1)]
    for i in range(n+1):
        score_mat[i][0] = i
	track_mat[i][0] = 'up'
    for i in range(m+1):
        score_mat[0][i] = i
	track_mat[0][i] = 'left'
    track_mat[0][0] = 0
    for row in range(n):
        for col in range(m):
            left = score_mat[row+1][col] + 1
            up = score_mat[row][col+1] + 1
            if sequence_1[row] == sequence_2[col]:
                    upper_left = score_mat[row][col] 
            else:
                    upper_left = score_mat[row][col] + 100
            score = [upper_left,left,up]
            track = ['upper_left','left','up']
            for i in range(3):
                    if score[i] < score_mat[row+1][col+1]:
                            score_mat[row+1][col+1] = score[i]
                            track_mat[row+1][col+1] = track[i]
    
    row,col = n,m
    seq_1,seq_2 = '',''
    while row != 0 or col != 0:
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
    seq_out = ''
    for i in xrange(len(seq_1)):
        if seq_1[i] == '-':
            seq_out = seq_out + seq_2[i]
        else:
            seq_out = seq_out + seq_1[i]
    return seq_out



if __name__ == '__main__':
    with open('/home/ycz/Rosalind/input/SCSP_in.txt', 'rb') as in_data:
        s = in_data.readline().strip()
        t = in_data.readline().strip()
    print EDTA(s,t)
