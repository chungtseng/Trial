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
    #print suf_dict
    return dna, k, suf_dict

def repeat_set(k,suf_dict):
    
    repeat = []
    def BFS_leaves(repeat,node,suf_dict):
        level = {node:0}
        parent = {node:None}
        frontier = [node]
        n = 0
        while frontier != []:
            next_level = []
            n += 1
            for i in frontier:
                for j in suf_dict:
                    if j[0] == i:
                        if j[1] in repeat:
                            break
                        level[j[1]] = n
                        parent[j[1]] = i
                        next_level.append(j[1])
            leaves = [ i for i in level if level[i] == n ]
            if len(leaves) >= k:
                break
            frontier = next_level[:]
        else:
            return
        return node
    for i in suf_dict:
        if i[0] not in repeat:
            temp = BFS_leaves(repeat,i[0],suf_dict)
            if temp == None:
                pass
            else:
                repeat.append(temp)
        else:
            pass
    return repeat
def LREP(dna,k,suf_dict):
    repeat = repeat_set(k,suf_dict)
    suffices = []
    for i in repeat:
        suffices.append(find_longest_suffix(i,suf_dict,dna))
        #print find_longest_suffix(i,suf_dict,dna)
    longest_substring = ''
    #print suffices
    for i in suffices:
        if len(i[1]) > len(longest_substring):
            longest_substring = i[1]
    return longest_substring

def find_longest_suffix(node,suf_dict,dna):
    level = {node:(0,'')}
    parent = {node:None}
    frontier = [node]
    while frontier != []:
        next_level = []
        for i in frontier:
            for key in suf_dict:
                if key[1] == i:
                    #print key
                    #print suf_dict[key]
                    level[key[0]] = level[i][0] + suf_dict[key][1], dna[suf_dict[key][0]-1:sum(suf_dict[key])-1] + level[i][1]
                    next_level.append(key[0])
        frontier = next_level
    #print level
    longest_suffix = ''
    longest_length = 0
    for key in level:
        if level[key][0] > longest_length:
            longest_length = level[key][0]
            longest_suffix = level[key][1]
    return longest_length,longest_suffix
            
    
if __name__ == '__main__':
    dna,k,suf_dict = parsing_suffix_tree('/home/ycz/Rosalind/input/LREP_in.txt')
    print LREP(dna,k,suf_dict)
