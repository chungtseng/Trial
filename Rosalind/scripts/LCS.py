import Fasta
fasta = Fasta.FASTA('/home/ycz/Rosalind/input/LCS.txt')
sequence = fasta.sequence()
dna_1 = sequence[0]
dna_2 = sequence[1]

def LCS(dna_1, dna_2):
	n_rows = len(dna_1) + 1
	n_columns = len(dna_2) + 1
	score_mat = [[0 for i in xrange(n_columns)] for j in xrange(n_rows)]
	track_mat = [[0 for i in xrange(n_columns)] for j in xrange(n_rows)]
	
	
	for i in xrange(n_rows-1):
		for j in xrange(n_columns-1):
			left = score_mat[i+1][j]
			up = score_mat[i][j+1]
			if dna_1[i] == dna_2[j]:	
				upper_left = score_mat[i][j] + 1
				score = [upper_left, left, up]
				track = ['upper-left','left','up']
			else:
				score = [left, up]				
				track = ['left','up']
			
			
			for k in xrange(len(score)):
				if score_mat[i+1][j+1] <= score[k]: # If this <= was <, because the initial score is 0, it might be equal to left or up.
					score_mat[i+1][j+1] = score[k]
					track_mat[i+1][j+1] = track[k]
	
	row = n_rows - 1
	col = n_columns - 1
	Longest_CS = ''
	while row != 0 and col != 0:
		if track_mat[row][col] == 'upper-left':
			Longest_CS = dna_1[row-1] + Longest_CS
			row -= 1
			col -= 1
		elif track_mat[row][col] == 'up':
			row -= 1
		elif track_mat[row][col] == 'left':
			col -= 1
	return Longest_CS
if __name__ == '__main__':
	with open('/home/ycz/Rosalind/output/LCS_out.txt','w+')	as output:
		output.write(LCS(dna_2, dna_1))
	
				
