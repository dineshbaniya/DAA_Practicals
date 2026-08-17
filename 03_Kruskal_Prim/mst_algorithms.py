def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]


def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1


def kruskal_mst(vertices, edges):
    edges = sorted(edges, key=lambda x: x[2])

    parent = list(range(vertices))
    rank = [0] * vertices

    mst = []
    total_cost = 0

    for u, v, weight in edges:
        root_u = find(parent, u)
        root_v = find(parent, v)

        if root_u != root_v:
            mst.append((u, v, weight))
            total_cost += weight
            union(parent, rank, root_u, root_v)

        if len(mst) == vertices - 1:
            break

    return mst, total_cost


def prim_mst(graph, vertices):
    selected = [False] * vertices
    key = [float('inf')] * vertices
    parent = [-1] * vertices

    key[0] = 0
    total_cost = 0
    mst = []

    for _ in range(vertices):
        minimum = float('inf')
        u = -1

        for v in range(vertices):
            if not selected[v] and key[v] < minimum:
                minimum = key[v]
                u = v

        selected[u] = True

        if parent[u] != -1:
            mst.append((parent[u], u, key[u]))
            total_cost += key[u]

        for v, weight in graph[u]:
            if not selected[v] and weight < key[v]:
                key[v] = weight
                parent[v] = u

    return mst, total_cost


# Graph used in the experiment
vertices = 6

edges = [
    (0, 1, 4),
    (0, 2, 3),
    (1, 2, 1),
    (1, 3, 2),
    (2, 3, 4),
    (2, 4, 2),
    (3, 4, 3),
    (3, 5, 2),
    (4, 5, 3)
]

graph = [[] for _ in range(vertices)]

for u, v, weight in edges:
    graph[u].append((v, weight))
    graph[v].append((u, weight))


# Kruskal's Algorithm
kruskal_result, kruskal_cost = kruskal_mst(vertices, edges)

print("Kruskal's Algorithm:")
for u, v, weight in kruskal_result:
    print(f"{u} - {v} : {weight}")

print("Total Cost:", kruskal_cost)


# Prim's Algorithm
prim_result, prim_cost = prim_mst(graph, vertices)

print("\nPrim's Algorithm:")
for u, v, weight in prim_result:
    print(f"{u} - {v} : {weight}")

print("Total Cost:", prim_cost)