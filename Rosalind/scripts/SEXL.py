with open('/home/ycz/Rosalind/input/SEXL_in.txt','rb') as in_data:
    A = map(float,in_data.readline().strip().split(' '))

B = []
for i in A:
    B.append(i*(1-i)*2)

print ' '.join(map(str,B))
