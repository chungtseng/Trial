import os
mass_dict = {}
with open(os.path.dirname(os.path.realpath(__file__)) + '/input/monoisotopic_mass_table.txt', 'r') as input_data:
	for line in input_data:
		linex = line.split('   ')
		mass_dict[linex[0]] = float(linex[1].strip('\n'))
def SPEC(L):
	L.sort()
	diff = []
	pr = ''
	for i in xrange(len(L)-1):
		diff.append(L[i+1] - L[i])
	for i in diff:
		for key in mass_dict:
			if abs(mass_dict[key]-i) <= 0.01:
				pr = pr + key
				break
	return pr
	
if __name__ == '__main__':
	import os
	L = []
	with open(os.path.dirname(os.path.realpath(__file__)) + '/input/SPEC_in.txt', 'r') as input_data:
		for line in input_data:
			L.append(float(line.strip('\n')))
	print SPEC(L)