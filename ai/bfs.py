#bfs
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : [],
  'F' : []
}

visited = [] 
queue = []     

def bfs(visited, graph, node): 
  visited.append(node)
  queue.append(node)

  while queue:          
    popped = queue.pop(0) 
    for neighbour in graph[popped]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
  return visited
print("BFS:")
print(bfs(visited, graph, 'A'))