input = """

CATACATAC$
2
node1 node2 1 1
node1 node7 2 1
node1 node14 3 3
node1 node17 10 1
node2 node3 2 4
node2 node6 10 1
node3 node4 6 5
node3 node5 10 1
node7 node8 3 3
node7 node11 5 1
node8 node9 6 5
node8 node10 10 1
node11 node12 6 5
node11 node13 10 1
node14 node15 6 5
node14 node16 10 1

""".strip('\n').split('\n')

# for large input, use the following instead:
#input = open("input.txt").read().strip('\n').split('\n')

dna, k, tree = input[0], int(input[1]), [ t.split() for t in input[2:] ]
nodes =  set([ t[0] for t in tree ] + [ t[1] for t in tree ])

# cache children of each node
children = dict()
for t in tree:
    for node in (t[0],t[1]):
        if node not in children:
            children[node] = []
    children[t[0]] += [t[1]]

# compute label of each edge
labels = dict()
for n1,n2,p1,p2 in [ (t[0],t[1],int(t[2]),int(t[3])) for t in tree ] :
    labels[(n1,n2)]= dna[ p1 - 1 :  p1 - 1 + p2 ]

node_substring = dict()
nb_leaves = dict()

# does two things: 
# - annotate each node with its label from the root
# - count the number of leaves below this node
def traverse(node, label = ""):
    node_substring[node] = label
    count_leaves = 1 if len(children[node]) == 0 else 0
    for neighbor in children[node]:
        count_leaves += traverse(neighbor, label + labels[(node,neighbor)])
    nb_leaves[node] = count_leaves
    return count_leaves

traverse('node1')

longest_substring = ""
for node in nodes:
    if nb_leaves[node] >= k:
        if len(node_substring[node]) > len(longest_substring):
            longest_substring = node_substring[node]

print longest_substring
