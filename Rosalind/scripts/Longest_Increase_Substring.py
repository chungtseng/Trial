def LIS(l):
    l_rec = [0 for i in range(len(l))]
    Lis = ['inf']
    for i in xrange(len(l)):
        for j in xrange(0,i):
            if l[j] < l[i]:
                l_rec[i] += 1
    for i in xrange(max(l_rec),0,-1):
        for j in xrange(len(l)-1,-1,-1):
            if l_rec[j] == i and l[j] < min(Lis):
                Lis.append(l[j])
                break
    del Lis[0]
    Lis = Lis[::-1]
    return Lis
    

if __name__ == '__main__':
    a = [1,2,3,2,23,234,34,5,436,43,32,4,3425,43,53,25,234532,45,21,4323,2,1,234,21]
    print LIS(a)
