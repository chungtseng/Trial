def read_conv(file_name):
    a = []
    b = []
    with open(file_name, 'rb') as in_data:
        a = in_data.readline().strip().split(' ')
        b = in_data.readline().strip().split(' ')
    return a,b
def CONV(a,b):
    import itertools
    difference = []
    prod = itertools.product(a,b)
    for i,j in prod:
        difference.append(round(float(i) - float(j),5))
        
    count = {}
    for i in difference:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    #print count
    max_key = 0
    max_val = 0
    for i in count:
        if count[i] > max_val:
            max_val = count[i]
            max_key = i
    return max_val, max_key

if __name__ == '__main__':
    a,b = read_conv('/home/ycz/Rosalind/input/CONV_in.txt')
    print CONV(a,b)
