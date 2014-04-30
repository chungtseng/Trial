#!/bin/user/env python
def read_input(file_name):
    dna = []
    with open(file_name, 'rb') as in_data:
        for line in in_data:
            dna.append(line.strip())
    dna = ''.join(dna)
    suffs = [dna[i:] for i in xrange(len(dna)-1,-1,-1)]
    return suffs

def com_pre_exist(l):
    if l == [''] or l == []:
        return False
    for i in xrange(len(l)):
        for j in [k for k in range(len(l)) if k > i]:
            if l[i][0] != l[j][0]:
                return False
    else:
        return True
    
def TRIE(dna):
    from copy import deepcopy
    global n
    if len(dna) == 1:
        if dna[0] != '':
            print dna[0]
        n += 1
	return
    dna_dict = {}
    rr = n
    for i in dna:
	if i[0] not in dna_dict:
	    dna_dict[i[0]] = [i[1:]]
	elif i[1:] != []:
	    dna_dict[i[0]] += [i[1:]]
    while True:
        update_dna_dict = deepcopy(dna_dict)
        for i in dna_dict:
            if com_pre_exist(dna_dict[i]):
                del update_dna_dict[i]
                #print dna_dict
                update_dna_dict[i+dna_dict[i][0][0]] = [k[1:] for k in dna_dict[i] if len(k) > 1]
                dna_dict = deepcopy(update_dna_dict)
                break
        else:
            break
        
    for key in dna_dict:
	n += 1
        if key != '':
            print  key
	TRIE(dna_dict[key])
    return

if __name__ == '__main__':
    suffs = read_input('/home/ycz/Rosalind/input/SUFF_in.txt')
    n = 1
    TRIE(suffs)
