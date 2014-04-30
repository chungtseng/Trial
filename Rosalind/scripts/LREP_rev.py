def parsing_suffix_tree(file_name):
    dna = ''
    k = 0
    suf_dict = {}
    with open(file_name, 'rb') as in_data:
        for ind, line in enumerate(in_data):
            if ind == 0:
                dna = line.strip()
            elif ind == 1:
                k = int(line.strip())
            else:
                linex = line.strip().split(' ')
                suf_dict[tuple(linex[0:2])] = tuple(map(int,linex[2:]))
    return dna, k, suf_dict

def children_gen(suf_dict):
    children = {}
    for key in suf_dict:
        if key[0] not in children:
            children[key[0]] = []
        children[key[0]] += [key[1]]
    return children

def labels_gen(dna,suf_dict):
    labels = {}
    for key in suf_dict:
        if key not in labels:
            labels[key] = dna[suf_dict[key][0]-1: suf_dict[key][0] -1 + suf_dict[key][1]]
    return labels

def traverse_tree(node,label,leaves_count,suffix,children,labels):
    suffix[node] = label
    if node not in children:
        count_leaves = 1
    else:
        count_leaves = 0
        for i in children[node]:
            count_leaves += traverse_tree(i, label + labels[(node,i)], leaves_count, suffix,children,labels)
    leaves_count[node] = count_leaves
    return count_leaves


if __name__ == '__main__':
    dna,k,suf_dict = parsing_suffix_tree('/home/ycz/Rosalind/input/LREP_in.txt')
    leaves_count = {}
    suffix = {}
    longest_substring = ''
    children = children_gen(suf_dict)
    labels = labels_gen(dna,suf_dict)
    traverse_tree('node1','',leaves_count,suffix,children,labels)
    #print leaves_count
    #print labels
    for node in leaves_count:
        if leaves_count[node] >= k:
            if len(suffix[node]) > len(longest_substring):
                longest_substring = suffix[node]
    print longest_substring
        
