import Fasta
ecr = Fasta.FASTA('/home/ycz/Rosalind/input/ecr.txt')
sequence = ecr.sequence()
seq_dict = {}
def rev_con(s):
	con_dict = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
	rev_con_s = ''
	for i in s:
		rev_con_s += con_dict[i]
	rev_con_s = rev_con_s[::-1]
	return rev_con_s
for i in sequence:
	try:
		seq_dict[i] += 1
	except KeyError:
		try:
			seq_dict[rev_con(i)] += 1
		except KeyError:
			seq_dict[i] = 1
corr_seq = []
incorr_seq = []
for key in seq_dict.keys():
	if seq_dict[key] >= 2:
		corr_seq.append(key)
	else:
		incorr_seq.append(key)
def ham_dist(s1, s2):
	if len(s1) == len(s2):
		hd = 0
		for i in xrange(len(s1)):
			if s1[i] != s2[i]:
				hd += 1
	else:
		return
	return hd

def find_corr(incorr_seq, corr_seq):
	corr_set = []
	for inc in incorr_seq:
		for cor in corr_seq:
			if ham_dist(inc,cor) == 1:
				corr_set.append(inc + '->' + cor)
				break
			elif ham_dist(inc, rev_con(cor)) == 1:
				corr_set.append(inc + '->' + rev_con(cor))
				break
	return corr_set
corr_set = find_corr(incorr_seq, corr_seq)
with open('/home/ycz/Rosalind/output/ecr_output.txt','w+') as output:
	output.write('\n'.join(corr_set))
