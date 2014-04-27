seqs = """
ATAGA
ATC
GAT
""".split()

nodes = [''] + list( set( [ seq[:i] for seq in seqs for i in xrange(1,len(seq)+1)] ) )
print nodes
from itertools import permutations
for node1, node2 in permutations(nodes,2):
    if node2[:-1] == node1:
        print "%d %d %c"%(nodes.index(node1)+1, nodes.index(node2)+1, node2[-1])
