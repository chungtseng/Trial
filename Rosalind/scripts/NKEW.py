def newick_dist(newick,a,b):
    import re
    taxa = [a,b]
    toks = re.split('([(),:])',newick)
    tokens = iter(re.split('([(),:])',newick))
    #print toks
    n = 1
    while next(tokens) not in taxa:
        pass
        n += 1
    climbs = 0
    descents = 0
    dist = 0
    for ind,token in enumerate(tokens):
        if token in taxa:
            break
        if token in ',)' and token != '':
            if descents > 0:
                descents -= 1
                dist = dist - int(toks[ind+n-1])
            else:
                climbs += 1
                dist += int(toks[ind+n-1])
        if token in ',(' and token != '':
            descents += 1
            ls = 0
            rs = 0
            for i in xrange(ind+n+1,len(toks) -1):
                if toks[i] in ',':
                    lolo=0
                elif toks[i] == '(':
                    ls += 1
                elif toks[i] == ')':
                    rs += 1
                if toks[i] not in ',' and ls == rs:
                    if toks[i] == ')':
                        num_i = i+3
                    else:
                        num_i = i+2
                    break
            dist += int(toks[num_i])
    return climbs + descents, dist
def newick_reader(filename):
    newick = []
    nodes = []
    with open(filename, 'rb') as input_data:
        for line in input_data:
            if ';' in line:
                newick.append(line.strip('\r\n'))
            elif line.strip('\r\n') != '':
                nodes.append(tuple(line.strip('\r\n').split(' ')))
    
    return newick, nodes    
    
def tmain():
    newick,nodes = newick_reader('/home/ycz/Rosalind/input/NKEW_in.txt')
    results = []
    print type(nodes[0][0])
    for ind,ite in enumerate(newick):
        results.append(newick_dist(ite,nodes[ind][0],nodes[ind][1]))
    for i in results:
        print i[1],
    return [i[1] for i in results]
if __name__ == '__main__':
    tmain()
