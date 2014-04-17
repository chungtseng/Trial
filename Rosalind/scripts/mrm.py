dna = 'TGGTTACCTG'
p = 1.0
for i in dna:
	if i in 'CG':
		p *= 0.509638/2
	else:
		p *= (1.0 - 0.509638)/2
print 1 - (1-p)**85032
	
