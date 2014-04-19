

if __name__ == '__main__':
	with open('/home/ycz/Rosalind/input/SETO.txt', 'r') as input_data:
		for ind,line in enumerate(input_data):
			if ind == 0:
				n = int(line.strip('\n'))
				U = set(map(str,range(1,n+1)))
			elif ind == 1:
				A = set(line.strip('\n{}').split(', '))
			elif ind == 2:
				B = set(line.strip('\n{}').split(', '))
	with open('/home/ycz/Rosalind/output/SETO_out.txt', 'w+') as output_data:
		output_data.write('{%s}\n' %(', '.join(map(str, A|B))))
		output_data.write('{%s}\n' %(', '.join(map(str, A&B))))
		output_data.write('{%s}\n' %(', '.join(map(str, A-B))))
		output_data.write('{%s}\n' %(', '.join(map(str, B-A))))
		output_data.write('{%s}\n' %(', '.join(map(str, U-A))))
		output_data.write('{%s}\n' %(', '.join(map(str, U-B))))