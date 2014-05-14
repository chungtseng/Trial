def DBG(s):
    results = []
    for i in s:
        results.append((i[0:len(i) - 1],i[1:len(i)]))
    return results

if __name__ == '__main__':
    S = []
    with open('Rosalind/input/dbj_in.txt','rb') as in_data:
        for line in in_data:
            S.append(line.strip())
    bound = dict(zip('ATCG','TAGC'))
    rc = lambda seq: ''.join([bound[i] for i in seq[::-1]])
    Src = map(rc, S)
    print Src
    S = set(S)
    Src = set(Src)
    s_t = S | Src
    a = DBG(s_t)
    with open('Rosalind/output/dbj_out.txt', 'w+') as out_data:
        for i in a:
            out_data.write('(%s, %s)\n' %(i[0],i[1]))
            
