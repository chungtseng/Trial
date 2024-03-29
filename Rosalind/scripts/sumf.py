import Fasta
sumf = Fasta.FASTA('/home/ycz/Rosalind/input/sumf.txt')
sequence = sumf.sequence()[0]
n = len(sequence)
s1 = sequence[0]
P = [0] * n
ind = 0
while ind != n-1:
	ind += 1
	if sequence[ind] == s1:
		if P[ind] < 1:
			P[ind] = 1
		for j in xrange(1, n-ind):
			if sequence[ind + j] != sequence[j]:
				#ind += j - 1
				break
			else:
				if P[ind + j] < j + 1:
					P[ind + j] = j + 1
		else:
			break
Ps = map(str, P)
with open('/home/ycz/Rosalind/output/sumf.txt', 'w+') as output:
	output.write(' '.join(Ps))

#NB's code
dna = ReadFASTA('data/rosalind_kmp.txt')[0][1]

P = [0]*len(dna)
k = 0
for q in range(2, len(dna)):
    while k > 0 and dna[k] != dna[q-1]: # This step checks substring of substring.
        k = P[k-1]
    if dna[k] == dna[q-1]:
        k += 1
    P[q-1] = k

print ' '.join(map(str, P))
with open('output/037_KMP.txt', 'w') as output_data:
output_data.write(' '.join(map(str, P)))
