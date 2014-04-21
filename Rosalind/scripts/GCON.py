def GCON(pr_1, pr_2):
	score_dict = {}
	with open('/home/ycz/Rosalind/input/BLOSUM62.txt') as mat:
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
	#gap penalty is constant 5. Score is assigned based on a matrix.
	score_mat_lon = [[float('-inf') for i in xrange(n_columns)] for j in xrange(n_rows)]
	score_mat_hor = [[float('-inf') for i in xrange(n_columns)] for j in xrange(n_rows)] #Mind the pointer system in mutable data structures!!!!!!!!!!!!
	score_mat[0][0] = 0
	score_mat_hor[0][0] = 0
	score_mat_lon[0][0] = 0
	for i in xrange(1,n_rows):
		score_mat_lon[i][0] = -5
		#score_mat[i][0] = -5
		score_mat_hor[i][0] = float('-inf')
	for i in xrange(1,n_columns):
		score_mat[0][i] = -5
		#score_mat_hor[0][i] = -5
		score_mat_lon[0][i] = float('-inf')
	
	for i in xrange(n_rows-1):
		for j in xrange(n_columns-1):
			score_mat_hor[i+1][j+1] = max(score_mat[i+1][j] - 5, score_mat_hor[i+1][j])
			score_mat_lon[i+1][j+1] = max(score_mat[i][j+1] - 5, score_mat_lon[i][j+1])
			score_mat[i+1][j+1] = max(score_mat[i][j]+ score_dict[pr_1[i]+pr_2[j]],score_mat_hor[i+1][j+1],score_mat_lon[i+1][j+1])
	return score_mat[n_rows-1][n_columns-1]



if __name__ == '__main__':
    from FASTA import FASTA
    fasta = FASTA('/home/ycz/Rosalind/input/GCON_in.txt')
    seqs = fasta.sequences()
    result = GCON(seqs[0],seqs[1])
    #print seqs
    print(result)
    #with open('/home/ycz/Rosalind/output/GLOB_out.txt','w+') as output:
    #    output.write('\n'.join(map(str,result)))
