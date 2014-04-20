MOTZ_number = {}
def MOTZ_num(rna):
	if len(rna) <= 1:
		return 1
	elif rna in MOTZ_number:
		return MOTZ_number[rna]
	bounding = dict(zip('AUCG','UAGC'))
	splits = [i for i in xrange(1, len(rna)) if rna[0] == bounding[rna[i]]]
	motz = MOTZ_num(rna[1:]) + sum([MOTZ_num(rna[1:i])*MOTZ_num(rna[i+1:]) for i in splits])
	MOTZ_number[rna] = motz
	return motz

if __name__ == '__main__':
	from FASTA import FASTA
	fasta = FASTA('/home/ycz/Rosalind/input/MOTZ_in.txt')
	seq = fasta.sequences()[0]
	print MOTZ_num(seq) % 10**6