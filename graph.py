E1 = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D', 'F'],
    'E': ['F']}

E2 = {
    "1": ["2", "3"],
    "2": ["3"],
    "3": ["7", "8"],
    "4": ["5", "7", "8"],
    "5": ["6", "8"],
    "6": ["8"],
    "7": ["8"]}

E3 = {
    "A" : ["B", "C", "D"]
}

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None


# print(find_path(E1, 'A', 'D'))
# print(find_all_paths(E1, "A", "D"))

def graph_to_edges(graph):
    E = []

    for e in graph:
        for v in graph[e]:
            E.append((e, v))

    return E


def adjacency_mat(graph):
    """
    Compute the adjacency matrix of a given graph
    Input : graph; assumed to list all of its vertices
    Output : adjacency matrix of the input graph
    """
    E = graph_to_edges(graph)

    V = []
    for (v1, v2) in E:
        if v1 not in V:
            V.append(v1)
        if v2 not in V:
            V.append(v2)

    A = [[0]*len(V)]*len(V)

    # for i, v1 in enumerate(V):
    #     for j, v2 in enumerate(V):
    #         if (v1, v2) in E:
    #             print(i, j, v1, v2)
    #             A[i][j] = 1

    for v1 in V:
        l = V.index(v1)
        for v2 in V:
            c = V.index(v2)
            print((v1, v2) in E, l, c, v1, v2)
            if (v1, v2) in E:
                A[l][c] = 1
                A[c][l] = 1


            print(A[l][c])




    # for v in set()
    print(V)
    print(E)
    print(A)

    return A

adjacency_mat(E3)
