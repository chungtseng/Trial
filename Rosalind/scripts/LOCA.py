def GLOB(pr_1, pr_2):
	score_dict = {}
	with open('/home/ycz/Rosalind/input/PAM250.txt') as mat:
            for ind,line in enumerate(mat):
                if ind == 0:
                    aa = line.strip(' \n').split('  ')
                    ind_dict = dict(zip(range(len(aa)),aa))
                else:
                    mat_score = filter(lambda i: i != '',line[1:].strip(' \n').split(' '))
                    #print mat_score
                    for col, ite in enumerate(mat_score):
                        score_dict[ind_dict[ind-1]+ind_dict[col]] = int(ite)
        print len(score_dict)
	n_rows = len(pr_1) + 1
	n_columns = len(pr_2) + 1
	score_mat = [[float('-inf') for i in xrange(n_columns)] for j in xrange(n_rows)]
	track_mat = [[0 for i in xrange(n_columns)] for j in xrange(n_rows)]
        track_mat[0][0] = 'start'
	#gap penalty is linearly 5. Score is assigned based on a matrix.
#	for i in xrange(n_rows):
#		score_mat[i][0] = -5 * 0
#	for i in xrange(n_columns):
#		score_mat[0][i] = -5 * 0
	for i in xrange(n_rows-1):
            for j in xrange(n_columns-1):
                start = 0
                left = score_mat[i+1][j] - 5
                up = score_mat[i][j+1] - 5
                upper_left = score_mat[i][j] + score_dict[pr_1[i]+pr_2[j]]
                score = [start, upper_left, left, up]
                track = ['start','upper-left','left','up']
			
                for k in xrange(len(score)):
                    if score_mat[i+1][j+1] <= score[k]: # If this <= was <, because the initial score is 0, it might be equal to left or up.
                        score_mat[i+1][j+1] = score[k]
                        track_mat[i+1][j+1] = track[k]
        max_score = float('-inf')
        for i in xrange(len(score_mat)):
            for j in xrange(len(score_mat[0])):
                if score_mat[i][j] > max_score:
                    max_score = score_mat[i][j]
                    max_ind = (i,j)
        i,j = max_ind
        s1 = ''
        s2 = ''
        while track_mat[i][j] != 'start':
            if track_mat[i][j] == 'upper-left':
                s1 = pr_1[i-1] + s1
                s2 = pr_2[j-1] + s2
                i -= 1
                j -= 1
            elif track_mat[i][j] == 'left':
                s2 = pr_2[j-1] + s2
                j -= 1
            elif track_mat[i][j] == 'up':
                s1 = pr_1[i-1] + s1
                i -= 1
	return max_score,s1,s2



if __name__ == '__main__':
    from FASTA import FASTA
    fasta = FASTA('/home/ycz/Rosalind/input/LOCA_in.txt')
    seqs = fasta.sequences()
    result = GLOB(seqs[0],seqs[1])
    print seqs
    for i in result:
        print i
    #with open('/home/ycz/Rosalind/output/GLOB_out.txt','w+') as output:
    #    output.write('\n'.join(map(str,result)))
