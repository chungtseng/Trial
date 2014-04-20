def check_noncrossing(rna,i):
	bounding = dict(zip('AUCG','UAGC'))
	if rna[0] != bounding[rna[i]]:
		return False
	count1 = map(rna[1:i].count, 'AUCG')
	count2 = map(rna[i+1:].count, 'AUCG')
	check_count = lambda count: count[0] == count[1] and count[2] == count[3]
	return check_count(count1) and check_count(count2)
	
catalan = {}
def cat_num(rna):
	if len(rna) <= 2:
		return 1
	if rna in catalan:
		return catalan[rna]
	splits = [i for i in xrange(1,len(rna)) if check_noncrossing(rna,i)]
	catalan_num = sum([cat_num(rna[1:i])*cat_num(rna[i+1:]) for i in splits])
	catalan[rna] = catalan_num
	return catalan_num
	
		
	

if __name__ == '__main__':
	from FASTA import FASTA
	fasta = FASTA('/home/ycz/Rosalind/input/CAT_in.txt')
	seq = fasta.sequences()[0]
	print cat_num(seq)