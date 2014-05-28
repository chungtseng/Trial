def conv(s1,s2):
    results = []
    for i in s1:
        for j in s2:
            results.append(round(float(i)-float(j),2))
    return results

def PRSM(n,seqs,R):
    max_mult = {}
    for i in seqs:
        #print i
        spec = complete_spectrum(i)
        convolution = conv(R,spec)
        max_mult[i] = max([convolution.count(j) for j in convolution])
    max_pr = [0,0]
    #print max_mult
    for key in max_mult:
        if max_mult[key] > max_pr[0]:
            max_pr[0] = max_mult[key]
            max_pr[1] = key
    return max_pr

def complete_spectrum(s):
    import os
    mass_dict = {}
    with open(os.path.dirname(os.path.realpath(__file__)) + '/input/monoisotopic_mass_table.txt', 'r') as input_data:
	for line in input_data:
            linex = line.split('   ')
            mass_dict[linex[0]] = float(linex[1].strip())
    S = []
    for i in xrange(1,len(s)):
        S.append(sum([mass_dict[s[j]] for j in xrange(0,i)]))
        S.append(sum([mass_dict[s[j]] for j in xrange(i,len(s))]))
    return S
            
if __name__ == '__main__':
    import re
    raw = []
    with open('/home/ycz/Rosalind/input/PRSM_in.txt','rb') as in_data:
        for line in in_data:
            raw.append(line.strip())
    n = raw[0]
    seqs = [pr for pr in raw if re.match('[A-Z]',pr)]
    R = [w for w in raw if re.match('[^A-Z]',w) and '.' in w]
    a = PRSM(n,seqs,R)
    print a[0]
    print a[1]
    #print seqs, R
