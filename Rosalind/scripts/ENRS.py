def ENRS(n, sequence, A):
	def comb_numb(n,k):
		result = 1
		if k > n/2:
			k = n-k
		for i in xrange(n-k+1, n+1):
			result *= i
		for i in xrange(1,k+1):
			result /= i
		return result
	B = []
	for i in A:
		p = 1.0
		for c in sequence:
			if c in 'CG':
				p *= i/2
			else:
				p *= (1-i)/2
		B.append((n-1)*p)
	return B

if __name__ == '__main__':
	with open('/home/ycz/Rosalind/input/ENRS_in.txt','r') as input_data:
		for ind,line in enumerate(input_data):
			if ind == 0:
				n = int(line[:-1])
			if ind == 1:
				sequence = line[:-1]
			if ind == 2:
				A = map(float,line[:-1].split(' '))
	with open('/home/ycz/Rosalind/output/ENRS_out.txt','w+') as output_data:
		for i in ENRS(n, sequence, A):
			output_data.write(str(i) + ' ')