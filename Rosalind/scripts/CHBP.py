def CHBP(taxa,chartb):
    import re
    sub_trees = []
    level = 2
    while True:
        current = []
        for i in chartb:
            if i.count('1') == level:
                currnet.append([l for l in xrange(len(taxa)) if i[l] == '1'])
            elif i.count('0') == level:
                current.append([l for l in xrange(len(taxa)) if i[l] == '0'])
        else:
            break
        level += 1
        sub_trees.append(current)
    results = sub_trees[0]
    for i in sub_trees[1:]:
        for ind,ite in enumerate(results):
            ele = [i for i in str(ite) if re.match('[1-9]',i)]


def CHBP_2(species, lines):
    from copy import deepcopy
    reduced = True
    while reduced:
        reduced = False
        tmp_lines = deepcopy(lines)
        for ch in lines:
            for switch in "01":
                if ch.count(switch) == 2:
                    i1 = ch.find(switch)
                    i2 = ch.find(switch, i1 + 1)
                    species[i1] = "(" + species[i1] + "," + species[i2] + ")"
                    species = species[:i2] + species[i2 + 1:]
                    lines.remove(ch)
                    reduced = True
                    for i, c in enumerate(lines):
                        lines[i] = lines[i][:i2] + lines[i][i2 + 1:]
                    break
    print "(" + ",".join(species) + ")"

if __name__ == '__main__':
    chrtb = []
    with open('/home/ycz/Rosalind/input/CHBP_in.txt','rb') as in_data:
        taxa = in_data.readline().strip().split(' ')
        for line in in_data:
            chrtb.append(line.strip())
    
    print CHBP_2(taxa,chrtb)
