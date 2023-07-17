# dfs
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : [],
  'F' : []
}

visitedNode = []

def dfs(node):
  if node not in visitedNode:
      visitedNode.append(node)
      for neighbour in graph[node]:
          dfs(neighbour)
  return(visitedNode)

print("DFS: ")
print(dfs('A'))

