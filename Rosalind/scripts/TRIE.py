#!/bin/user/env python
def read_input(file_name):
    dna = []
    with open(file_name, 'rb') as in_data:
        for line in in_data:
            dna.append(line.strip())
    return dna
def TRIE(dna):
    global n
    if len(dna) == 1:
	for i in dna[0]:
	    print '%d %d %s' %(n, n+1, i)
	    n += 1
	return
    dna_dict = {}
    rr = n
    for i in dna:
	if i[0] not in dna_dict:
	    dna_dict[i[0]] = [i[1:]]
	elif i[1:] != []:
	    dna_dict[i[0]] += [i[1:]]
	    
    for key in dna_dict:
	n += 1
	print '%d %d %s' %(rr, n, key)
	TRIE(dna_dict[key])
    return

if __name__ == '__main__':
    dna = read_input('/home/ycz/Rosalind/input/TRIE_in.txt')
    n = 1
    TRIE(dna)
