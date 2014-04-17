def MOTZ(rna):
	bounding = dict(zip('AUCG','UAGC'))
	non_crossing_matching = {}
	def count_non_crossing_matching(rna):
		if len(rna) <= 1:
			return 1
		elif rna in non_crossing_matching:
			return non_crossing_matching[rna]
		splits = [i for i in xrange(1,len(rna)) if rna[i] == bounding[rna[0]]]
		non_crossing_matching[rna] = sum([count_non_crossing_matching(rna[1:i])*count_non_crossing_matching(rna[i+1:]) for i in splits]) + count_non_crossing_matching(rna[1:])
		return non_crossing_matching[rna]
	return count_non_crossing_matching(rna)
		
	

if __name__ == '__main__':
	from FASTA import FASTA
	fasta = FASTA('/home/ycz/Rosalind/input/MOTZ_in.txt')
	seq = fasta.sequences()
	print MOTZ(seq[0]) % 10**6
	