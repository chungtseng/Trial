import Fasta
tt_input = Fasta.FASTA('/home/ycz/Rosalind/input/tt.txt')
sequence = tt_input.sequence()
tt_dict = {'AT': 'transversion', 'AC': 'transversion', 'GC': 'transversion', 'GT': 'transversion', 'AG': 'transition', 'CT': 'transition'}
for i in tt_dict.keys():
	kr = i[::-1]
	tt_dict[kr] = tt_dict[i]
transversion = 0
transition = 0
for i in range(len(sequence[0])):
	try:
		if tt_dict[sequence[0][i]+sequence[1][i]] == 'transversion':
			transversion += 1
		else:
			transition += 1
	except KeyError:
		pass
result = float(transition)/float(transversion)
print result
	
