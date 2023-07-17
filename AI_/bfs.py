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

def bfs(node): 
  queue.append(node)
  while queue:          
    popped = queue.pop(0) 
    if popped not in visited:
      visited.append(popped)
      for neighbour in graph[popped]:
        queue.append(neighbour)
  return visited
print("BFS:")
print(bfs('A'))