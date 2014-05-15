def FULL(c_mass,start,end):
    import os
    mass_dict = {}
    with open(os.path.dirname(os.path.realpath(__file__)) + '/input/monoisotopic_mass_table.txt', 'r') as input_data:
	for line in input_data:
            linex = line.split('   ')
            mass_dict[linex[0]] = float(linex[1].strip())
    ptn = ''
    ptn_mass = 0
    for i in c_mass:
        for j in mass_dict:
            if abs(i - ptn_mass - mass_dict[j] - start) <= 0.01:
                ptn += j
                ptn_mass = sum([mass_dict[chr] for chr in ptn])
    return ptn
    
if __name__ == '__main__':
    spectrum = []
    with open('/home/ycz/Rosalind/input/FULL_in.txt', 'rb') as in_data:
        for line in in_data:
            spectrum.append(float(line.strip()))
    p_mass = spectrum[0]
    c_mass = spectrum[1:]
    start = min(c_mass)
    end = max(c_mass)
    c_mass.remove(start)
    c_mass.remove(end)
    print FULL(c_mass,start,end)
    
    
