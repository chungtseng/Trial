s = 'TCTGAGCTGGAAAAGTGACCCTTGATAGTCACGCTCTACTCACTAAGTTTACACTCACGCTATCAAACCAGCTAAAACCCACG'
A = '0.108 0.147 0.179 0.264 0.331 0.359 0.438 0.485 0.526 0.562 0.646 0.699 0.769 0.793 0.868 0.907'
Ax = A.split(' ')
def log10_P_rand_DNA(s, GC):
	import math
	PN = {'A':(1-GC)/2, 'G':GC/2}
	PN['T'] = PN['A']
	PN['C'] = PN['G']
	logP = 0.0
	for i in s:
		logP += math.log10(PN[i])
	return str(logP)
R = {}

for ind,ite in enumerate(Ax):
	R[ind] = log10_P_rand_DNA(s, float(ite))

with open('/home/ycz/Rosalind/output/rs_out.txt', 'w+') as output:
	output.write(' '.join(R.values()))
