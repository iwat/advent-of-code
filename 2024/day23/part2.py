import collections
import functools
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


@functools.cache
def find_mesh(encoded_mesh):
    valid_mesh = [nodes[name] for name in encoded_mesh.split(',')]

    last_node = valid_mesh[-1]
    sorted_mesh = ','.join([m.name for m in sorted(valid_mesh, key=lambda m: m.name)])

    best_mesh = None
    for candidate_member in last_node.neighbors:
        valid_candidate = True
        for existing_member in valid_mesh:
            if existing_member not in candidate_member.neighbors:
                valid_candidate = False
                break
        if valid_candidate:
            mesh = find_mesh(sorted_mesh + ',' + candidate_member.name)
            if best_mesh is None or len(mesh) > len(best_mesh):
                best_mesh = mesh

    if best_mesh is not None:
        return best_mesh
    return ','.join(sorted([member.name for member in valid_mesh]))


longest_mesh = None
for node_1 in nodes.values():
    mesh = find_mesh(node_1.name)
    if longest_mesh is None or len(mesh) > len(longest_mesh):
        longest_mesh = mesh
print(longest_mesh)
