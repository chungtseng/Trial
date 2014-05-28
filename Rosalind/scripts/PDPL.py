from collections import Counter
def PDPL(L):
    dist = Counter(L)
    X = {0}
    width = max(dist)
    tmp_dist = lambda e, S: Counter(abs(e-s) for s in S)
    contained = lambda a, b: all(a[x] <= b[x] for x in a)
    while len(dist) > 0:
        ele = max(dist)
        if contained(tmp_dist(ele,X),dist):
            X |= {ele}
            dist -= tmp_dist(ele,X)
        else:
            X |= { width - ele }
            dist -= tmp_dist(width-ele,X)
            
    return X
            

if __name__ == '__main__':
    with open('/home/ycz/Rosalind/input/PDPL_in.txt','rb') as in_data:
        L = map(int,in_data.readline().strip().split(' '))
    print ' '.join(map(str,sorted(list(PDPL(L)))))
        
