def newick_dist(newick,a,b):
    if a == b:
        return 0
    data = newick.replace(',',' ').replace('(','( ').replace(')',' )').strip(';').split()
    for i in xrange(len(data)):
        if a in data[i]:
            a_ind = i
        if b in data[i]:
            b_ind = i
    counter = 0
    f_num = 0
    r_num = 0
    change_level = 1
    level = 0
    
    for i in xrange(min(a_ind,b_ind),max(a_ind,b_ind)):
        if data[i][0] == '(':
            counter += 1
            counter = abs(counter)
            change_level += 1
            level += 1
        elif data[i][0] == ')':
            counter += 1
            counter = abs(counter)
            change_level += 1
            level -= 1
        elif change_level != 0:
            if level != 0:
                counter += 1 + change_level
            else:
                counter -= 1 + change_level
            change_level = 0
    return abs(counter)
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
    newick,nodes = newick_reader('/home/ycz/Rosalind/input/NWCK_in.txt')
    results = []
    for ind,ite in enumerate(newick):
        results.append(newick_dist(ite,nodes[ind][0],nodes[ind][1]))
    for i in results:
        print i,
