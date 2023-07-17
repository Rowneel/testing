graph = {
    'S': [('A', 12), ('B', 4)],
    'A': [('C', 7), ('D', 3)],
    'B': [('E', 8), ('F', 2)],
    'F': [('I', 9), ('G', 0)],
    'E': [('H',4)]
}

goal="G"
visitedNode = []
queue = []

def gbfs(start):
    queue.append(start)
    while queue:
        queue.sort(key=lambda x: x[1])
        popped = queue.pop(0)
        if popped not in visitedNode:
            visitedNode.append(popped)
            if popped[0] == goal:
                break
            for neighbor in graph[popped[0]]:
                queue.append(neighbor)
    return visitedNode
print("Gready Best First is:")
print(gbfs(('S', 13)))