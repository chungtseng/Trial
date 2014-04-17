def MULT(seq_list):
	seq_dict = {}
	length_dict = {}
	for ind, ite in enumerate(seq_list):
		seq_dict[ind] = ite
		length_dict[ind] = len(ite)
	def score_create(n):
		if n == 0:
			return [float('-inf') for i in range(length_dict[n]+1)]
		else:
			score = [score_create(n-1)[:] for i in range(length_dict[n]+1)]
		return score
	# Have to initiate the score matrix. Then, score is calculated in (*,*,*,*) situations.

if __name__ == '__main__':
	from FASTA import FASTA
	fasta = FASTA('/home/ycz/Rosalind/input/MULT_in.txt')
	seqs = fasta.sequences()
	MULT(seqs)