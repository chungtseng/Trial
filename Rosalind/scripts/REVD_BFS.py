def count_breakpoint(L):
	#Return break points indices (start of a consecutive block) and number of beak points.
	break_points = []
	for i in xrange(len(L)-1):
		if abs(L[i+1] - L[i]) != 1:
			break_points.append(i+1)
	#print 'b   ' , break_points
	return len(break_points)


def greedy_BFS_rev_dist(identity, perm):
	id_dict = dict(zip(identity, range(1,len(identity)+1)))
	normalized_perm = [0] + [id_dict[i] for i in perm] + [len(identity)+1]
	#print normalized_perm
	rev_operation = lambda perm, i, j: perm[0:i] + perm[j:i-1:-1] + perm[j+1:]
	level = {tuple(normalized_perm):None}
	frontier = [normalized_perm]
	dist = 0
	min_bp = float('inf')
	while True:
                next_perms = []
		dist += 1
		for check_perm in frontier:
			break_points = count_breakpoint(check_perm)
			if break_points == 0:
				return dist-1
			for i in range(1,len(identity)):
				for j in [k for k in range(1,len(identity)+1) if k > i]:
					temp_perm = rev_operation(check_perm,i,j)
					#print 'p    ' , temp_perm
					temp_bp = count_breakpoint(temp_perm)
					if temp_bp == 0:
						return dist
					if tuple(temp_perm) not in level:
						level[tuple(temp_perm)] = dist
						next_perms.append(temp_perm)
		#print next_perms
		frontier = next_perms[:]


if __name__ == '__main__':
	perms = []
	with open('/home/ycz/Rosalind/input/SORT_in_2.txt', 'r') as input_data:
		for line in input_data:
			if len(line) != 1:
				linex = line.strip('\n').split(' ')
				perms.append(map(int,linex))
	
	#print perms
	for i in range(0,10,2):
		print greedy_BFS_rev_dist(perms[i],perms[i+1])
