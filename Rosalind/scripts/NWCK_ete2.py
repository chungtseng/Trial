def newick_dist(newick,a,b):
    import re
    taxa = [a,b]
    tokens = iter(re.split('([(),])',newick))
    while next(tokens) not in taxa:
        pass
    climbs = 0
    descents = 0
    dist = 0
    for token in tokens:
        if token in taxa:
            break
        if token in ',)':
            if descents > 0:
                descents -= 1
                
            else:
                climbs += 1
        if token in ',(':
            descents += 1
    return climbs + descents
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
    
if __name__ == '__main__':
    newick,nodes = newick_reader('/home/ycz/Rosalind/input/NKEW_in.txt')
    results = []
    print type(nodes[0][0])
    for ind,ite in enumerate(newick):
        results.append(newick_dist(ite,nodes[ind][0],nodes[ind][1]))
    for i in results:
        print i,
