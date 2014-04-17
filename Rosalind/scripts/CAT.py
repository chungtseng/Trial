def catalan_num(rna):
	bounding = dict(zip('AUCG','UAGC'))
	non_crossing_bounding = {}
	def check_non_crossing(rna,i):
		count_1 = map(rna[1:i].count,'AUCG')
		count_2 = map(rna[i+1:].count,'AUCG')
		return count_1[0] == count_1[1] and count_1[2] == count_1[3] and count_2[0] == count_2[1] and count_2[2] == count_2[3]
	def count_non_crossing(rna):
		if len(rna) <= 2:
			return 1
		elif rna in non_crossing_bounding:
			return non_crossing_bounding[rna]
		splits = [ i for i in xrange(1,len(rna),2) if check_non_crossing(rna,i)]
		non_crossing_bounding[rna] = sum([count_non_crossing(rna[1:i]) * count_non_crossing(rna[i+1:]) for i in splits])
		return non_crossing_bounding[rna]
	return count_non_crossing(rna)

if __name__ == '__main__':
	from FASTA import FASTA
	fasta = FASTA('/home/ycz/Rosalind/input/CAT_in.txt')
	rna = fasta.sequences()[0]
	print catalan_num(rna)%10**6