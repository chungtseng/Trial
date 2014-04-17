def edit_distance(pr_1, pr_2):
	#Use score matrix to record the number of edit moves. Choose from the least moves.
	n = len(pr_1)
	m = len(pr_2)
	score_mat = [[200000 for i in range(m+1)] for j in range(n+1)]
	track_mat = [[200000 for i in range(m+1)] for j in range(n+1)]
	for i in range(n+1):			#In the number 0 row or column, moving down or right adds one edit move.
		score_mat[i][0] = i
	for i in range(m+1):
		score_mat[0][i] = i
	for i in xrange(n):
		for j in xrange(m):
			left = score_mat[i+1][j] + 1
			up = score_mat[i][j+1] + 1
			if pr_1[i] == pr_2[j]:	
				upper_left = score_mat[i][j]
				score = [upper_left, left, up]
				track = ['upper-left-a','left','up']
			else:
				upper_left = score_mat[i][j] + 1
				score = [upper_left, left, up]	
				track = ['upper-left-s','left','up']
			for k in xrange(len(score)):
				if score_mat[i+1][j+1] >= score[k]: # If this <= was <, because the initial score is 0, it might be equal to left or up.
					score_mat[i+1][j+1] = score[k]
					track_mat[i+1][j+1] = track[k]
	#print score_mat
	#print '-------------------------'
	#for i in track_mat:
	#	print i
	
	row = n
	col = m
	ed = 0
	Longest_CS = ''
	while row != 0 and col != 0:
		if track_mat[row][col] == 'upper-left-a':
			Longest_CS = pr_1[row-1] + Longest_CS
			row -= 1
			col -= 1
		elif track_mat[row][col] == 'upper-left-s':
			row -= 1
			col -= 1
			ed += 1
		elif track_mat[row][col] == 'up':
			row -= 1
			ed += 1
		elif track_mat[row][col] == 'left':
			col -= 1
			ed += 1
	#print row
	#print col
	if row != 0:
		ed += row
	elif col != 0:
		ed += col
	return ed
if __name__ == '__main__':
	import Fasta
	fasta = Fasta.FASTA('/home/ycz/Rosalind/input/EDTA.txt')
	sequences = fasta.sequence()
	pr_1 = sequences[0]
	pr_2 = sequences[1]
	print edit_distance(pr_1, pr_2)

