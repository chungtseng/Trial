def RNAS(rna):
    bound = dict(zip('AC','UG'))
    bound['G'] = 'CU'
    bound['U'] = 'AG'
    if rna in rna_dict:
        return rna_dict[rna]
        
    if len(rna) <= 4:
        return 1
    rna_dict[rna] = sum([RNAS(rna[1:i]) * RNAS(rna[i+1:]) for i in xrange(4,len(rna)) if rna[i] in bound[rna[0]]]) + RNAS(rna[1:])
    return rna_dict[rna]
    
    

if __name__ == '__main__':
    with open('/home/ycz/Rosalind/input/RNAS_in.txt','rb') as in_data:
        rna = in_data.readline().strip()
    print rna
    rna_dict = {}
    print RNAS(rna)
