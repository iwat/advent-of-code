import collections
import sys

Node = collections.namedtuple('Node', ['name', 'neighbors'])

nodes = {}
for line in [l.strip() for l in sys.stdin.readlines()]:
    a, b = line.split('-')
    if a in nodes:
        node_a = nodes[a]
    else:
        node_a = Node(a, [])
        nodes[a] = node_a
    if b in nodes:
        node_b = nodes[b]
    else:
        node_b = Node(b, [])
        nodes[b] = node_b
    node_a.neighbors.append(node_b)
    node_b.neighbors.append(node_a)

trios = set()
for node_1 in nodes.values():
    for node_2 in node_1.neighbors:
        for node_3 in node_2.neighbors:
            if node_1 in node_3.neighbors:
                trios.add(tuple(sorted([node_1.name, node_2.name, node_3.name])))

for trio in trios:
    found = False
    for m in trio:
        if m[0] == 't':
            found = True
            break
    if found:
        print(trio)
