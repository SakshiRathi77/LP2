class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

def kruskal(graph):
    n = len(graph)
    disjoint_set = DisjointSet(n)
    edges = []
    minimum_spanning_tree = []

    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j] != 0:
                edges.append((i, j, graph[i][j]))

    edges.sort(key=lambda x: x[2])

    for edge in edges:
        src, dest, weight = edge
        if disjoint_set.find(src) != disjoint_set.find(dest):
            disjoint_set.union(src, dest)
            minimum_spanning_tree.append((src, dest, weight))

    return minimum_spanning_tree

# Example usage
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

minimum_spanning_tree = kruskal(graph)

print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    src, dest, weight = edge
    print(f"{src} - {dest}: {weight}")
