def aStarAlgo(start_node, stop_node):
    open_set = set([start_node])
    g = {start_node: 0}
    parents = {start_node: start_node}

    while open_set:
        n = min(open_set, key=lambda node: g[node] + heuristic(node))

        if n == stop_node:
            path = []
            while n != start_node:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            return path

        open_set.remove(n)

        for (m, weight) in Graph_nodes[n]:
            if m not in g or g[n] + weight < g[m]:
                g[m] = g[n] + weight
                parents[m] = n
                open_set.add(m)

    return None

def heuristic(n):
    H_dist = {'S': 5, 'A': 3, 'B': 4, 'C': 2, 'D': 6, 'G': 0}
    return H_dist[n]

Graph_nodes = {
    'S': [('A', 1), ('G', 10)],
    'A': [('B', 2), ('C', 1)],
    'B': [('D', 5)],
    'C': [('D', 3), ('G', 4)]
}

path = aStarAlgo('S', 'G')
if path:
    print('A* search algorithm')
    print('Path found:', path)
else:
    print('Path does not exist!')
