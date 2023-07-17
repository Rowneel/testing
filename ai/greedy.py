graph = {
    'A': [('B', 5), ('D', 12)],
    'B': [('A', 9), ('C', 4)],
    'C': [('D', 4), ('B', 7)],
    'D': [('A', 9), ('C', 5)]
}

goal="D"

def gbfs(graph, start):
    queue = [start]
    visitedNode = []

    while queue:
        queue = sorted(queue, key=lambda x: x[1])
        node = queue.pop(0)

        if node not in visitedNode:
            visitedNode.append(node)

            if node[0] == goal:
                break

            neighbors = graph[node[0]]

            for neighbor in neighbors:
                queue.append(neighbor)
                
    return visitedNode
print("Gready Best First is:")
print(gbfs(graph, ('A', 15)))