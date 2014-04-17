vl = []
vr = []
n = 0
with open('/home/ycz/Rosalind/input/ct.txt', 'r') as input:
	for line in input:
		linex = line.split(' ')
		if len(linex) == 1:
			total_nodes = int(linex[0])
		else:
			vl.append(linex[0])
			vr.append(linex[1][:-1])
adj_dict = {}
for i in xrange(len(vl)):
	if vl[i] in adj_dict:
		adj_dict[vl[i]] = adj_dict[vl[i]] + ',' + vr[i]
	else:
		adj_dict[vl[i]] = vr[i]
init_sets = []
for key in adj_dict.keys():
	init_sets.append(set([key] + adj_dict[key].split(',')))
final_sets = []
while True:
	if init_sets == []:
		break
	n = 1
	while n != len(init_sets):
		if init_sets[0] & init_sets[n] == set([]):
			n += 1
		else:
			init_sets[0] |= init_sets[n]
			del init_sets[n]
	final_sets.append(init_sets[0])
	del init_sets[0]
nb = len(final_sets)
conn_nodes = 0
for i in final_sets:
	conn_nodes += len(i)
nsingle = total_nodes - conn_nodes
result = nsingle + nb - 1
print result

	


