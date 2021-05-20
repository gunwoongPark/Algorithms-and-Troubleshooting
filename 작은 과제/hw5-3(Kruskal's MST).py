# 1
parent = dict()
rank = dict()
def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]
def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

# 2
def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)
    minimum_spanning_tree = set()
    edges = list(graph['edges'])
    edges.sort()
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)
    return sorted(minimum_spanning_tree)

# 3
graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'edges': set([(6, 'A', 'B'),
                  (9, 'A', 'J'),
                  (6, 'B', 'J'),
                  (5, 'B', 'D'),
                  (8, 'B', 'H'),
                  (11, 'C', 'G'),
                  (9, 'C', 'F'),
                  (7, 'D', 'J'),
                  (6, 'D', 'I'),
                  (8, 'E', 'G'),
                  (11, 'E', 'F'),
                  (6, 'G', 'H'),
                  (7, 'H', 'I'),
                  (8, 'I', 'J'),
                  (6, 'I', 'B'),
                  (7, 'I', 'E'),
                  (11, 'J', 'F'),
                  (9, 'H', 'C'),
                  (5, 'E', 'D'),
                  (9, 'G', 'F')
                  ])
}

print(kruskal(graph))